
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
			"links": name_only + extension,
		})
	return pages

def jinja2_templating(template_html,file_name,title_name):
	from jinja2 import Template
	pages = content_files()
	content_html = open(file_name).read() #file_name variable created for the file paths see above
	template_html = open("templates/base.html").read() #open template base.html
	template = Template(template_html) #function Template w/ pmtr template_html assigned to template var
	return template.render(      #key step for placeholders
	title=title_name,
	content=content_html,
	pages=pages,
	)

def main():
	pages = content_files()
	template_html = open("templates/base.html").read() #opens base.html
	for page in pages:
		docs_output(template_html,page) 

def docs_output(template_html,page): 
	file_name = page['filename']  
	output = page['output']
	title_name = page['title']
	links = page['links']
	final_step = jinja2_templating(template_html,file_name,title_name) #helper function
	open(output, "w+").write(final_step) 


if __name__ == '__main__':
	main() #invokes the main function


