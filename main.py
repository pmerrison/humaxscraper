__author__ = 'Paul Merrison'

import re

from bs4 import BeautifulSoup


class episode:
    title = ''
    filename = ''
    defn = ''

# response = urllib.request.urlopen("http://10.0.1.2/browse/index.jim?dir=/media/My%20Video/Sarah%20%26%20Duck")
#output = response.read()
#output = open('C:\Users\Paul\Desktop/sandd.html')
soup = BeautifulSoup(open("sandd.html"))
ts_tags = soup.find_all(type="ts")
table = []
for tag in ts_tags:
    this_episode = episode()

    if tag is not None:
        #Get the episode name
        groups = re.match(r'.*title="(.*):', str(tag))
        if groups is not None:
            this_episode.title = groups.group(1)
            #print(tag)
        #Get whether it's HD or not
        groups = re.match(r'.*(\[HD\]).*', str(tag))
        if groups:
            this_episode.defn = "HD"
        else:
            this_episode.defn = "SD"
        #Get the file name
        groups = re.match(r'.*(Sarah%20%26%20Duck_\S+.ts)', str(tag))
        if groups:
            episode_string = groups.group(1).strip()
            episode_string = episode_string.replace('%20', ' ')
            episode_string = episode_string.replace('%26', '&')
            this_episode.filename = episode_string

    if this_episode.title is not '':
        table.append(this_episode)

f = open("output.csv", 'w')
for row in table:
    assert isinstance(row, episode)

    f.write(row.title + "," + row.defn + "," + row.filename + '\n')
#tag = soup.a
#print(soup.find_all('a'))
#print(soup.get_text())
#for line in output:
#    if re.match(r'.* Sarah .*', str(line)):
#        print(line)

"""
<a class=bf title="Tortoise Snooze: Animation. When it is time for Tortoise to hibernate, Sarah and Duck help him find a quiet place to sleep. [HD] [AD,S]"
		    file="/media/My%20Video/Sarah%20%26%20Duck/New_%20Sarah%20%26%20Duck_20141014_1714.ts" type=ts href=#>
		    New_ Sarah & Duck_20141014_1714.ts
	        </a>
	        """

"""
<a class="bf" file="/media/My%20Video/Sarah%20%26%20Duck/Sarah%20%26%20Duck_world%20bread%20day_20131030_1811.ts" href="#" title=
"World Bread Day: Animation. When there's a bread festival in the park, Sarah and Duck find themselves part of an exciting treasure hunt. [
AD,S]" type="ts">
		    Sarah &amp; Duck_world bread day_20131030_1811.ts

" file="/media/My%20Video/Sarah%20%26%20Duck/Sarah%20%26%20Duck_20150217_1711.ts" href="#" title="Toy Tidy: Animation. Duck has been
leaving his toys everywhere, so Sarah decides to assist him with tidying his bedroom. [HD] [AD,S]" type="ts">
Sarah &amp; Duck_20150217_1711.ts
		    """
