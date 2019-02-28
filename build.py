#1.) Simplify repetitive parts by creating variables, do this for page kayes
#2.) Determine what needs to be done, in this case:
# - Access the base file
# - Replace the placeholders with content files
# - Direct the new file to the output folder
#3.) Per the requirements of the homework use this three steps to create three functions
#4.) Group the line items by readibility and efficiency (title and content placeholder in one fx + return stmnt)
#5.) Make sure to have the right parameters for each function to avoid undefined terms errors within your
#        local function

	#Created a list of dictionaries of the files involved, the directory to which the output should go
	#and the title which will eventually be used for the placeholder
pages = [
	{
		"filename":"content/index.html",
		"output":"docs/index.html",
		"title":"Home"
	},
	{
		"filename":"content/FeatureProject.html",
		"output":"docs/FeatureProject.html",
		"title":"Feature Project"
	},
	{
		"filename":"content/Publication.html",
		"output":"docs/Publication.html",
		"title":"Publication"
	},

	] 

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


