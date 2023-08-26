from pytube import YouTube

def get_title(url):
    return YouTube(url).title()


def submit_link_vocal(*args, **kwargs):
    link_vocal = Element('link-vocal').element.value 
    Element('output-vocal-link').write(link_vocal)
    print("Vocal link: ", link_vocal)

    # Unable to get title of a video
    # urllib.error.URLError: <urlopen error unknown url type: https
    # title_vocal = get_title(link_vocal)
    # Element('ouptut-vocal-title').write(title_vocal)
    # print("Title: ", title_vocal)

def submit_link_instrument(*args, **kwargs):
    link_instrument = Element('link-instrument').element.value 
    Element('output-instru-link').write(link_instrument)
    print("Instrumental link: ", link_instrument)