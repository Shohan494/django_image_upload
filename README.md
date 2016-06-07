# django_image_upload

#### A simple project for uploading images from the users made with [Django Web Framework](http://djangoproject.com), the web framework for perfectionists with deadlines.

# Followed References

This project was just done for learning purpose and I have followed these links:

#### Main Resource
* **http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example**
* **https://github.com/axelpale/minimal-django-file-upload-example**

#### Others
* http://stackoverflow.com/questions/8922056/what-is-the-best-way-to-upload-and-store-pictures-on-the-site
* http://www.tutorialspoint.com/django/django_file_uploading.htm

# Notes
* If anyone wants to uopload just any file they want, a little change will do the job. In the file **imagic/forms.py** change the code :
```
class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file'
    )
```
to this:
```
class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select an Image'
    )
```
and you are done!

* A little change had been made just to get rid of a syntax error due to django version upgrade. I used the latest version for this project which is [version - 1.9](https://docs.djangoproject.com/en/1.9/releases/1.9/). The edited file is **imagic/views.py**, watch out the comment in the code :
```
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            # takes the argument(reverse) as the name of the file paased in url.py
            # this line has been edited
            return HttpResponseRedirect(reverse('list'))
```         

**Happy Coding** :+1:
