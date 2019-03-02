
def content_files():
	import glob #finds pathnames matching a specified pattern
	import os #extracts useful parts of file paths

	all_html_files = glob.glob("content/*.html") #looks for a list of files w/ a pattern, .html
	pages = [] #builds from the contents of the content directory = content/*.html
	for html_file in all_html_files:
		file_path = html_file
		file_name = os.path.basename(file_path) #os in effect for file path extraction
		name_only, extension = os.path.splitext(file_name)

		pages.append({ #refactored version
			"filename": 'content/' + name_only + extension,
			"title": name_only,
			"output": 'docs/' + name_only + extension,
			"links": 'content/' + name_only + extension,
		})
		return(pages)

def jinja2_templating(file_name,title):
	from jinja2 import Template
	pages = content_files()
	content_html = open(file_name).read() #file_name variable created for the file paths see above
	template_html = open("templates/base.html").read() #open template base.html
	template = Template(template_html) #function Template w/ pmtr template_html assigned to template var
	return template.render(      
	title=title,
	content=content_html,
	pages=pages,
	)

def main():
	pages = content_files()
	template = open("templates/base.html").read() #opens base.html
	for page in pages:
		docs_output(template,page) 

def docs_output(template,page): #all the parameters are local, we need template and page as parameters to define them before using in fx locally
	filename = page['filename'] #lines 95 - 97 dictionary keys assigned to a variable 
	output = page['output']
	title = page['title']
	links = page['links']
	final_step = apply_template(template,filename,title,links) #helper function
	open(output, "w+").write(final_step) #overwrites the html file in the output with the file that has the placeholders replaced

def apply_template(template,filename,title,links): 
	index_content = open(filename).read() #opens filename and assign it to variable index_content
	finished_index_page = template.replace("{{content}}", index_content) #placeholder content is replaced with index_content
	finished_index_page = finished_index_page.replace("{{title}}", title) #placeholder title is replaced by title kep
	return (finished_index_page) #exits apply_template function, gives us a value, the desired file we want.


if __name__ == '__main__':
	main() #invokes the main function


