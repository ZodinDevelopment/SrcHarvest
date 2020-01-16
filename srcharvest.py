import os
import sys
import time
import requests
import urllib.request
import bs4 as bs

def main():
    os.system('clear')
    path_to_urls = str(input("Enter path to .txt file with urls >> "))
    filename = path_to_urls.split('.')[0]
    if not os.path.isfile(path_to_urls):
        print('Error! Invalid path!\n')
        time.sleep(0.5)
        raise Exception

    with open(path_to_urls, 'r') as f:
        urls_as_string = f.read()

    urls_as_list = urls_as_string.split('\n')

    print('{0} urls parsed from text file...'.format(str(len(urls_as_list))))
    time.sleep(0.5)

    for url in urls_as_list:
        print('[+] {0}'.format(url))
        time.sleep(0.1)

    print('Beginning scraping process.')
    time.sleep(0.4)
    urls_scraped = 0
    for url in urls_as_list:
        file_index = urls_scraped + 1
        filename_html = '{0}_{1}.html'.format(filename, str(file_index))
        filename_imgs = '{0}_{1}_imgs.txt'.format(filename, str(file_index))
        print('{0}/{1} urls scraped.'.format(str(urls_scraped), str(len(urls_as_list))))
        print('-'* 24)
        print('Attempting to fetch data from: \n{}'.format(url))

        try:
            source = urllib.request.urlopen(url).read()

        except ValueError as e:
            print('Error parsing url strings.')
            print(str(e))
            continue
        except Exception as e:
            print('There was an error in making the request')
            print(str(e))
            continue

        soup = bs.BeautifulSoup(source, 'lxml')

        print('Successfully retrieved source code from url and parsed')
        time.sleep(0.5)
        
        

        #print('Saving source code as "{0}.html"'.format(pagename))
        #domain = url.split('/')[1]
        #if 'www' in domain.split('.'):
            #pagename = domain.split('.')[1]

        #else:
            #pagename = domain.split('.')[0]



        #filename = pagename + '.html'
        html_as_string = soup.prettify()

        print('Saving source code as {0}'.format(filename))

        with open(filename_html, 'w') as f:
            f.write(html_as_string)
        print('File save success')
        time.sleep(0.5)
        print('Attempting to retrieve image objects from parsed source...')
        time.sleep(0.5)
        imgs = soup.find_all('img')

        img_links = []
        print('{0} images found in source.'.format(str(len(imgs))))
        for img in imgs:
            img_src = img.attrs.get('src')
            if img_src is None:
                continue 
            img_link = url + img_src

            img_links.append(img_link)
        
        print('Saving parsed image urls to file "{0}"'.format(filename_imgs))
        with open(filename_imgs, 'w') as f:
            for link in img_links:
                f.write(link + '\n')

        print('Links saved.')
        time.sleep(0.5)
        input('Press enter to continue > ')
        time.sleep(0.2)
        urls_scraped += 1
    
    print('Out of the {0} urls read from file, \n{1} were successfully parsed and scraped for image objects.'.format(str(len(urls_as_list)), str(urls_scraped)))
    time.sleep(1.0)
    print('Script developed by Michael Landon / Zodin Development')
    time.sleep(0.1)
    print('GitHub: "https://github.com/ZodinDevelopment/')
    time.sleep(0.1)
    print('Developer Contact: michael.landon@zodin.dev')
    time.sleep(0.2)
    print('Thanks for using, come again!')
    time.sleep(0.4)

    sys.exit()


if __name__ == '__main__':
    main()

    
