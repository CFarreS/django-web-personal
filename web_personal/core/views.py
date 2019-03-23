from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href='/'>Portada</a></li>
    <li><a href='/portafolio/'>Portafolio</a></li>
    <li><a href='/about-me/'>Acerca de</a></li>
    <li><a href='/contact/'>Contacto</a></li>
</ul>
"""


# Create your views here.
def home(request):
    html_response = html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
        """
    # # Prova de for al back-end
    # html_response = '<h1>Mi web personal</h1>'
    # for i in range(10):
    #     html_response += '<h2>Portada</h2>'
    return HttpResponse(html_response)


def portafolio(request):
    html_response = html_base + """
        <h2>Portafolio</h2>
        <p>Estos son mis proyectos</p>
        """
    return HttpResponse(html_response)


def about(request):
    html_response = html_base + """
        <h2>Acerca de</h2>
        <p>Soc el Carles i soc el rei</p>
        """
    return HttpResponse(html_response)


def contact(request):
    html_response = html_base + """
        <h2>Contacto</h2>
        <p> Em deixeu un missatge: <a href='mailto:carles.f_95@outlook.es'> carles.f_95@outlook.es </a> </p>
        """
    return HttpResponse(html_response)

