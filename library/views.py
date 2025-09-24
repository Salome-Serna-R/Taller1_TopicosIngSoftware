from django.shortcuts import render
from .models import Content, Searches
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

# Create your views here.

def mental_health_library(request):
    topic = request.GET.get('topic')  # Obtenemos el tema seleccionado del formulario
    if topic:
        contents = Content.objects.filter(topic=topic)
        search = Searches(choice=topic)
        search.save()
    else:
        contents = Content.objects.all()

    context = {
        'contents': contents,
        'selected_topic': topic,
    }
    return render(request, 'library.html', context)

def search_statistics(request):
    matplotlib.use('Agg')
    topics = ['stress', 'depression', 'anxiety']
    search_per_topic_count = {}
    for topic in topics:
        search_in_topic = Searches.objects.filter(choice=topic)
        count = search_in_topic.count()
        search_per_topic_count[topic] = count

    bar_width = 0.5
    bar_spacing = 0.5
    bar_positions = range(len(search_per_topic_count))

    #crear la gráfica de barras
    plt.bar(bar_positions, search_per_topic_count.values(), width=bar_width, color="#8B74DB",align='center')
    #personalizar la grafica
    plt.title('Searches per Topic', fontsize=14, fontweight='bold')
    plt.xlabel('Topic', fontsize=12)
    plt.ylabel('Number of Searches', fontsize=12)
    plt.xticks(bar_positions, search_per_topic_count.keys(), rotation=45, fontsize=10)
    #ajustar el espaciado entre las barras
    plt.subplots_adjust(bottom=0.3)

    for i, v in enumerate(search_per_topic_count.values()):
        plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

    #guardar la grafica en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    plt.close()

    #convertir la grafica base 64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'statistics.html', {'graphic':graphic})
