from distutils.command.upload import upload
#from tinymce.models import HTMLField
#from froala_editor.widgets import FroalaEditor
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django import forms


class ConsultaForm(forms.Form):
    email = forms.EmailField(max_length=100, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        )
    nombres = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'})
    )
    apellidos = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'})
    )
    OPTIONS_DOCUMENT_TYPES = (
        ('DNI','DNI'),
        ('CE','CARNET DE EXTRANJERIA'),
        ('PAS','PASAPORTE'),
        )
    tipo_doc_identidad = forms.ChoiceField(required=True,choices=OPTIONS_DOCUMENT_TYPES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    nro_doc_identidad = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nro. Documento'})
    )
    organizacion = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organización'})
    )
    OPTIONS_DISTRITOS = (
        ('CUSCO','CUSCO'),
        ('SANTIAGO','SANTIAGO'),
        ('SAN SEBASTIAN','SAN SEBASTIAN'),
        ('SAN JERONIMO','SAN JERONIMO'),
        ('WANCHAQ','WANCHAQ'),
        ('CCORCA','CCORCA'),
        ('POROY','POROY'),
        ('SAYLLA','SAYLLA'),
        )
    distrito = forms.ChoiceField(required=True,choices=OPTIONS_DISTRITOS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    OPTIONS_OBSERVATION_TYPES = (
        ('OBSERVACION','OBSERVACION'),
        ('RECOMENDACION','RECOMENDACION'),
        )
    tipo_observacion = forms.ChoiceField(required=True,choices=OPTIONS_OBSERVATION_TYPES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    OPTIONS_DOCUMENTS = (
        ('CARACTERIZACION','CARACTERIZACION'),
        ('PROPUESTA','PROPUESTA'),
        )
    documento_observacion = forms.ChoiceField(
        required=True,
        choices=OPTIONS_DOCUMENTS, 
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    #observaciones = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, "class":"form-control", "placeholder":"Observaciones"}))
    
    observaciones = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px','data-user-id': 123456, 'data-device': 'iphone'}}))


    archivo_adjunto = forms.FileField(required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Archivo Adjunto'})
    )
    """ fecha_consulta = forms.DateTimeField(required=False,input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'col-3 form-control',
            'data-toggle': "datepicker"
        }))"""
    fecha_consulta = forms.DateTimeField(required=False,
        widget=forms.HiddenInput()       
    )


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Selecciona el archivo...')
    direccion = forms.CharField(max_length=100, required=False)