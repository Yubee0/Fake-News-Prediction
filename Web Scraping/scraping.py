from bs4 import BeautifulSoup
import requests

#guardian -real
url = [
   'https://thehimalayantimes.com/nepal/pm-warns-against-forces-bid-to-reverse-republicanism',
   'https://thehimalayantimes.com/nepal/ramchandra-paudel-sworn-in-as-third-president',
   'https://thehimalayantimes.com/nepal/nepals-newly-elected-president-takes-oath-of-office',
   'https://thehimalayantimes.com/nepal/election-officer-refuses-to-revoke-yadavs-candidacy',
   'https://thehimalayantimes.com/nepal/fsu-election-tu-bans-placement-of-poster-pamphlet-for-publicity',
  'https://thehimalayantimes.com/kathmandu/nembang-appointed-deputy-leader-of-uml-parliamentary-party',
   'https://thehimalayantimes.com/nepal/chitwan-2-by-election-parties-granted-symbols',
   'https://thehimalayantimes.com/sports/uml-chair-oli-calls-for-unity-to-end-vaw',
  'https://thehimalayantimes.com/kathmandu/vice-president-election-silence-period-commencing-from-midnight-today',
  'https://thehimalayantimes.com/kathmandu/pm-dahal-stresses-on-quality-education',
   
# ]

# cnn ---> error section tag vayako le
# url = 'https://edition.cnn.com/2022/02/10/politics/donald-trump-gop-incumbents-impeach-votes/index.html' ]

# bbc *
# # url =[
    'https://www.bbc.com/news/av/60334905',
   'https://www.bbc.com/news/world-asia-64957293',
   'https://www.bbc.com/news/world-us-canada-64939930',
   'https://www.bbc.com/news/world-asia-china-64959500',
   'https://www.bbc.com/news/world-australia-64945819',
   'https://www.bbc.com/news/world-australia-58635393',
   'https://www.bbc.com/news/world-europe-58614229',
   'https://www.bbc.com/news/world-europe-58610234',
   'https://www.bbc.com/news/world-europe-58600454',
   'https://www.bbc.com/news/business-64949786',
    # ]

#ratopati
# url ='https://www.ratopati.com/story/220582/2022/2/10/congress'

#kathmandu post ----> yesma error aayo
# url = 'https://kathmandupost.com/national/2022/02/10/will-people-from-kalapani-region-get-to-exercise-their-franchise'

#nepalnews -----> yesma paragraph lina sakena
# url = 'https://nepalnews.com.np/s/nation/mohp-records-1-369-new-covid-cases-12-deaths-on-thursday'

#online khabar
# url = 'https://www.onlinekhabar.com/2022/02/1077033'

#nytimes
# url = 'https://www.nytimes.com/2022/02/10/us/politics/jan-6-trump-calls.html'

#foxnews *
# url = [
    'https://www.foxnews.com/politics/democrats-scramble-reverse-course-covid-restrictions-midterms',
    'https://www.foxnews.com/politics/biden-announces-executive-order-expand-background-checks-calls-lawmakers-go-further',
    'https://www.foxnews.com/politics/ted-cruz-asks-stanford-punish-students-who-heckled-trump-judge',
    'https://www.foxnews.com/politics/air-force-diversity-equity-inclusion-hiring-spree-top-job',
    'https://www.foxnews.com/politics/north-carolina-democrat-wesley-harris-announces-his-run-treasurer-2024',
    'https://www.foxnews.com/politics/north-carolina-gov-cooper-announces-new-violence-prevention-office',
    'https://www.foxnews.com/politics/2024-poll-trump-desantis-neck-neck-among-republican-voters-gop-nomination-economy-top-issue?dicbo=v2-t5b16es',
    'https://www.foxnews.com/politics/nikki-haley-dings-desantis-trump-us-aid-ukraine-2024-gop-presidential-sweepstakes?dicbo=v2-ekpdefr',
    'https://www.foxnews.com/politics/arkansas-gov-sanders-signs-trans-care-malpractice-bill-law?dicbo=v2-lfh43dp',
    'https://www.foxnews.com/politics/gavin-newsom-hides-client-failed-silicon-valley-bank-statement-praising-bailout',
    # ]

#nbcnews ----> error occured
# url = 'https://www.nbcnews.com/news/world/u-s-intel-nine-probable-russian-routes-ukraine-full-scale-n1288922'

#gaurdians news*
# url = [
    'https://www.theguardian.com/football/2022/feb/10/chelsea-braced-for-kepa-arrizabalaga-bids-and-open-to-summer-exit',
    'https://www.theguardian.com/us-news/2023/mar/15/trump-media-investigated-possible-money-laundering',
    'https://www.theguardian.com/football/2023/mar/14/manchester-city-rb-leipzig-champions-league-last-16-second-leg-match-report',
    'https://www.theguardian.com/us-news/2023/mar/14/russian-fighter-jet-collides-us-drone-black-sea-crash',
    'https://www.theguardian.com/sport/2023/mar/14/honeysuckle-ends-career-with-mares-hurdle-win-at-cheltenham-festival',
    'https://www.theguardian.com/football/2023/mar/14/internazionale-hold-off-porto-to-reach-quarter-finals-for-first-time-in-12-years',
    'https://www.theguardian.com/world/2023/mar/15/pakistan-riot-police-fire-teargas-on-crowds-trying-to-prevent-arrest-of-imran-khan',
    'https://www.theguardian.com/business/2023/mar/13/silicon-valley-bank-why-did-it-collapse-and-is-this-the-start-of-a-banking-crisis',
    'https://www.theguardian.com/global-development/2023/mar/15/virus-outbreak-in-west-bengal-leaves-19-children-dead-and-thousands-in-hospital',
    ]

#abc news
# url = 'https://abcnews.go.com/Politics/pressure-builds-biden-democrats-move-past-covid/story?id=82754983'

# url = 'https://edition.cnn.com/2022/02/10/politics/biden-ukraine-things-could-crazy/index.html'



def getUrl(url): #get the response 
    pageContent = requests.get(url)
    print(pageContent)
    return pageContent

def parse(pagecontent):
    data = []
    if pagecontent.status_code != 200: #beside response 200 for all response show page not found
        print('Page not found')
        return 0
    coup = BeautifulSoup(pagecontent.content, 'html.parser') #Parse the content using bs4
    try:
        if coup.find('article') is not None: #if news article is in article tag
            print('article')
            contentParse = coup.find('article')

        

        elif coup.find('div') is not None: #if news article is in div tag
            print("div")
            #searching for the right div is left here
            contentParses = coup.find_all('div')
            # print(len(contentParses))
            # print('xir2')
            flag = 0
            for contentParse in contentParses:
                if contentParse.find('h1') is not None:
                    # print('xir3')
                    headline = contentParse.find('h1').text
                    # print(f'Title: {headline}')
                    break
                flag +=1
            count = 0
            newsArticles = contentParses[flag].find_all('p')
            for newsArticle in newsArticles:
                if count == 5:
                    break
                # print(newsArticle.text, end=' ')
                data.append(newsArticle.text)
                count +=1
            data.insert(0, headline)
            data = ' '.join(data)
            dictt = {
            # 'title': headline,
            'article': data
        }
            print(dictt)
            return dictt # to process only the article which is in div tag
        else:
            errormessage = 'No content found'
            print(errormessage)
        
# to process the article which is in article tag
        headline = contentParse.find('h1').text
        # print(f"Title: {headline}")

        newsArticles = contentParse.find_all('p')
    # print(len(newsArticles))

        for newsArticle in newsArticles:
            # print(newsArticle.text, end=' ')
            data.append(newsArticle.text)
        # dictt = {
        #     'title': headline,
        #     'article': data
        # }
        data.insert(0, headline)
        data = ' '.join(data)
        dictt = {
            'title': headline,
            'text': data
        }

        print(dictt)
        return dictt

    except: #any error occured during the process 
        print("Error Occured")

import csv
fieldnames = ['title','text']
with open('news.csv', 'a', newline='', encoding='utf-8') as csv_file:
    
    # csv_writer = csv.writer(csv_file)
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()   #---> for setting up the header for the csv file
    for lin in url:
        news = parse(getUrl(lin))
    # print()
    # print('printing for csv file: {}'.format(news['title']))
    # print()
    # print('printing for csv file: {}'.format(news['text']))
        
        csv_writer.writerow(news)
