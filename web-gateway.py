import os
import web
import yaml

from grey_matter import speak

render = web.template.render('templates/')
urls = (
    '/', 'index',
)

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']

speak('Welcome {}, systems are now ready to run. How can I help you?'.format(name))


class index:
    def GET(self):
        return render.index()

    def POST(self):
        x = web.input(myfile={})
        filedir = os.getcwd() + '/uploads'  # directory to store file in
        if 'myfile' in x:  # check if file object is created
            filepath = x.myfile.filename.replace('\\', '/')  # replaces windows slashes for linux
            filename = filepath.split('/')[-1]  # split commands and chose the las part (filename with extension)
            fout = open(filedir + '/' + filename, 'w')  # creates dir where the uploaded files should be stored
            fout.write(x.myfile.file.read())  # writes the uploaded file to the newly created one
            fout.close()  # close the file, upload complete
        os.system('python ai.py ' + filename)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
