
import glob
all_html_files = glob.glob("content/*.html") #glob looks for a list of files w/ names matching a pattern, .html
print(all_html_files)

import os #extracts useful parts of file paths

file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name) #prints blog.html
name_only, extension = os.path.splitext(file_name)
print(name_only) #prints blog

pages = [] #builds from the contents of the content directory = content/*.html
pages.append({
	"filename": "content/index.html",
	"title": "Index",
	"output": "docs/index.html",
})

print(pages) #lists the contents of the content folder in terminal  

def main():
	template = open("templates/base.html").read() #opens base.html
	for page in pages:
		docs_output(template,page) 

def docs_output(template,page): #all the parameters are local, we need template and page as parameters to define them before using in fx locally
	filename = page['filename'] #lines 95 - 97 dictionary keys assigned to a variable 
	output = page['output']
	title = page['title']
	final_step = apply_template(template,filename,title) #helper function
	open(output, "w+").write(final_step) #overwrites the html file in the output with the file that has the placeholders replaced

def apply_template(template,filename,title): 
	index_content = open(filename).read() #opens filename and assign it to variable index_content
	finished_index_page = template.replace("{{content}}", index_content) #placeholder content is replaced with index_content
	finished_index_page = finished_index_page.replace("{{title}}", title) #placeholder title is replaced by title kep
	return (finished_index_page) #exits apply_template function, gives us a value, the desired file we want.






if __name__ == '__main__':
	main() #invokes the main function


