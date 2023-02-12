from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import pyrebase
from time import sleep
from django.core.files.storage import FileSystemStorage

config = {
  'apiKey': "AIzaSyArHFLsk0pevFNMMGjVavppb5wltduzggw",
  'authDomain': "job-portal-c65be.firebaseapp.com",
  'projectId': "job-portal-c65be",
  'storageBucket': "job-portal-c65be.appspot.com",
  'messagingSenderId': "839506484975",
  'appId': "1:839506484975:web:a703ed5cef40c22f93451a",
  'measurementId': "G-584JGPMYSY",
'databaseURL': "https://job-portal-c65be-default-rtdb.europe-west1.firebasedatabase.app/",
}
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from firebase_admin import storage
from collections import OrderedDict
# Initialize the Firebase Storage client
firebase= pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()



def home(request):
    #jobdic_orig=db.child('Jobs').child('Job Detail').get().val()
    jobdic=  OrderedDict([('1001', {'Applicants': {'abubakarkhan99': {'coverletter_name': ' ctvgnjmkmjnhbvfcdxsxdgfvhnjmk,l', 'email_name': 'abubakar_khan_99@hotmail.com', 'eu_eligible_name': 'y', 'exp_name': '2', 'firstname_name': 'Hafiz', 'lastname_name': 'Khan', 'phonenum_name': '+46735625456', 'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FInternational%20Deferral%20Form%20-%20NCIRL.pdf?alt=media'}}, 'Req': {'company': 'Facebook', 'deadline': '01/03/2023', 'desc': '<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p>At Jobba in Gothenburg, Sweden we work with some of Sweden’s largest automotive manufacturers within research and development. Now we are looking to expand our team of automotive software test engineers. Within the field of testing, the trend is moving towards automation. Therefore, we are looking for you who are an automotive software test engineer or automotive software developer, preferably experienced with Python and Continuous Integration (CI/CD). Here, we encourage and support our engineers to evolve professionally as personally. Therefore, you will have the fullest support from your closest Jobba manager, who will follow you in your journey and support you forward – in the direction you want. When you feel like you want to learn something new, you can always take it into your own hands because Jobba Academy offers several educations, from new programming languages to negotiation skills and much more.</p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p>To be successful in this role, we believe that you have:</p> <ul><li>Minimum 5 years of experience working with automotive software, either testing or development.</li> <li>Professional experience working with Python or C++.</li> <li>Worked in an Agile environment.</li> <li>A relevant degree in Computer Science, Software Engineering, Electronics, Data Science, Mathematics, Physics or similar.</li> </ul><p>Meritorious experience:</p> <ul><li>Experience in PyTest or Robot Framework.</li> <li>Experience with CI/CD tools e.g. Jenkins.</li> <li>Experience with Vector tools e.g. CANoe, CANalyzer.</li> <li>Experience with CAN, LIN, Ethernet.</li> </ul><p>&nbsp;To succeed in the role as a consultant at Jobba you need to be analytical, have a great sense for quality, a positive attitude and you need to be a team-player. If You find this as an interesting next step and would like to get in touch with us, don’t hesitate to send in your application.&nbsp;</p> <p><strong>About JOBBA</strong></p> <p>Jobba is one of Europe’s largest technology and IT consulting companies with over 45,000 employees in over 30 countries. Our engineers carry out complex and highly technical projects throughout the value chain of the most prestigious companies in all sectors, such as Automotive, Telecom, Industry, Energy, Aerospace &amp; Defense and Life Science. In Sweden, we are over 1300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</p> <p>For the fourth year in a row, Jobba has been named one of Sweden\'s most attractive employers by Karriärföretagen 2023, an award for employers that offer unique career and development opportunities.</p> <p>Welcome to read more about us at&nbsp;<a href="#" target="_blank" rel="noreferrer noopener">jobba.se</a></p> <p>We are looking forward to your application!</p>    </div>', 'experience': '3+', 'expiry': '20/10/2023', 'id': '1001', 'loc': 'Menlo Park', 'postdate': '08/01/2019', 'salary': '110000', 'title': 'Data Scientist', 'type': 'Full time'}}), ('1002', {'Applicants': {'abubakarkhan99': {'coverletter_name': ' sdfhj,kl.ukyuyhrsrfwergtshyjufyjh', 'email_name': 'abubakar_khan_99@hotmail.com', 'eu_eligible_name': 'yes', 'exp_name': '2', 'firstname_name': 'Hafiz', 'lastname_name': 'Khan', 'phonenum_name': '+46735625456', 'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FInternational%20Deferral%20Form%20-%20NCIRL.pdf?alt=media'}}, 'Req': {'company': 'Amazon', 'deadline': '01/03/2023', 'desc': '<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">To fit into this role, you need to have a personality that exudes drive and proactivity. </font><font style="vertical-align: inherit;">You are a problem-solving oriented and positive person who enjoys working in teams to jointly reach the best solution.</font></font><br> &nbsp;</span></p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Now we have an opportunity for you who want to work in manufacturing. </font><font style="vertical-align: inherit;">The role is within production technology with a focus on PLC programming. </font><font style="vertical-align: inherit;">We are now looking for automation engineers with education or experience.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">As a consultant with us, you work with the main focus on PLC programming for one of our clients. </font><font style="vertical-align: inherit;">Furthermore, you get both a team feeling in your assignment and a really lovely community at Nordic Solutions. </font><font style="vertical-align: inherit;">Through our internal networks Nordic Solutions Sports, Women@Nordic Solutions and Nordic Solutions Innovation, you are given the opportunity to pursue issues and activities that you are passionate about, together with your colleagues. </font><font style="vertical-align: inherit;">Everything is of course voluntary. </font><font style="vertical-align: inherit;">We place balance between work and private life at the top of the list. </font><font style="vertical-align: inherit;">Of course, we have a collective agreement. </font><font style="vertical-align: inherit;">In addition to this, we have benefits such as health care allowance, occupational pension and insurance.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">We are looking for you as a manufacturing engineer as you join as a production technician with a focus on automation. </font><font style="vertical-align: inherit;">Together with other technicians in the area, you will drive technology development to reach the goals set for the area in the form of technical availability, production cost, ergonomics, volume and quality. </font><font style="vertical-align: inherit;">The role requires a genuine interest in technology, analytical ability and collaborative skills. </font><font style="vertical-align: inherit;">In the role, you have to manage stakeholders in the form of operators, production managers, PT colleagues, maintenance and suppliers.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The challenges are to drive improvement work together with other support functions at the same time in close cooperation with our customer\'s suppliers. </font><font style="vertical-align: inherit;">The service requires a technical understanding, but also an understanding to deliver the product at the right cost and quality.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Our customer has challenges regarding automation in several areas, which will also be part of the service to provide assistance and training for current employees. </font><font style="vertical-align: inherit;">Driving the technical development of automation requires technical curiosity, as well as good collaboration skills as it will always take place in consultation with several stakeholders. </font><font style="vertical-align: inherit;">This will require a great focus on getting to know the process and its parameters, as well as understanding how the process affects outcomes on the product but also subsequent processes. </font><font style="vertical-align: inherit;">Furthermore, it becomes a challenge to be in a factory during start-up, where routines are under construction, both with regard to the process itself, but also organizationally. </font><font style="vertical-align: inherit;">In other words, you must be prepared for changes to occur.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Training:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">University education in mechanical engineering/automation.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Production technical training meritorious.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Competency requirements:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PLC programming is a requirement.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Analytical ability. </font><font style="vertical-align: inherit;">Ability to understand and break down complex problems when troubleshooting, for example. </font><font style="vertical-align: inherit;">Genuine technical interest, as this is an area of \u200b\u200brapid technological development.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Good cooperation skills with other technicians, maintenance but also understanding of operators, production managers and their requirements for delivery.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Meritorious:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge of CNC controllers and robot handling.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge in vision technology.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Experience of working within highly automated flows.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Swedish in both speech and writing.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">English in both speech and writing.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Characteristics/values</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Documented, thorough, quality conscious &amp; committed.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Good cooperation skills.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Technically interested in machines and processes.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Strong personal drive.</font></font></li> </ul><p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">What do we offer?</font></font></strong></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Every employee is equally important in Nordic Solutions\'s success! </font><font style="vertical-align: inherit;">We believe in growing together by offering opportunities, development and community. </font><font style="vertical-align: inherit;">Nordic Solutions operates in several different industries, has a large variety of assignments, coaching managers and training via the Nordic Solutions Academy, which means that it will always be possible to develop with us. </font><font style="vertical-align: inherit;">Your wishes guide your path forward. </font><font style="vertical-align: inherit;">Through our internal networks such as Women@Nordic Solutions and Nordic Solutions Sports, you are given the opportunity to pursue issues and activities that you are passionate about. </font><font style="vertical-align: inherit;">At Nordic Solutions, we think it is important to have a balance between work and leisure, which is why we offer three extra days off per year. </font><font style="vertical-align: inherit;">With us, you are connected to a collective agreement and are offered benefits such as health benefits, occupational pension and insurance.</font></font></p> <p>&nbsp;<strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Om OLD</font></font></strong></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Nordic Solutions is one of Europe\'s largest technology and IT consulting companies with over 45,000 employees in more than 30 countries. </font><font style="vertical-align: inherit;">Our engineers carry out complex and highly technical projects throughout the entire product development chain at the leading companies in several different industries such as Automotive, Telecom, Industry, Energy, Aviation and Defense as well as Life Science. </font><font style="vertical-align: inherit;">In Sweden, we are over 1,300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">For the third year in a row, Nordic Solutions has been named one of Sweden\'s most attractive employers by Career Companies 2022, an award for employers that offer unique career and development opportunities.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Welcome to read more about us at&nbsp; </font></font><a href="https://www.Nordic Solutions.se/" target="_blank" rel="noreferrer noopener"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Nordic Solutions.se</font></font></a></p> <p>&nbsp;</p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A warm welcome with your application!</font></font></p>    </div>', 'experience': '5+', 'expiry': '20/10/2023', 'id': '1002', 'loc': 'Seattle', 'postdate': '08/01/2019', 'salary': '130000', 'title': 'Production Techniques - Automation', 'type': 'Full time'}}), ('1003', {'Req': {'company': 'Microsoft', 'deadline': '01/03/2023', 'desc': 'As an AI Engineer at Microsoft, you will work on building and deploying advanced AI and machine learning systems. You will collaborate with a team of researchers and engineers to develop cutting-edge algorithms, and implement them in real-world applications. Minimum qualifications include a bachelors degree in Computer Science, Electrical Engineering, or a related field, and 2+ years of experience in AI or machine learning.', 'experience': '2+', 'expiry': '20/10/2023', 'id': '1003', 'loc': 'Redmond', 'postdate': '08/01/2019', 'salary': '100000', 'title': 'AI Engineer', 'type': 'Full time'}}), ('1004', {'Req': {'company': 'Amazon', 'deadline': '01/03/2023', 'desc': 'The DevOps Engineer will be responsible for designing, implementing, and maintaining the infrastructure and tools to support the development and deployment of software. You will work closely with development teams to understand their needs and provide solutions to improve the overall software delivery process. The ideal candidate will have experience with cloud infrastructure, automation, and continuous integration/delivery.', 'experience': '5+', 'expiry': '20/10/2023', 'id': '1004', 'loc': 'Seattle', 'postdate': '08/01/2019', 'salary': '130000', 'title': 'DevOps Engineer', 'type': 'Full time'}}), ('1006', {'Req': {'company': 'Microsoft', 'deadline': '01/03/2023', 'desc': 'The AI Engineer will be responsible for designing, developing and deploying AI-based solutions to improve various aspects of the Microsoft product and services. You will work closely with cross-functional teams to understand business needs, identify opportunities, and deliver data-driven solutions. The ideal candidate will have a background in computer science or a related field, and have experience in machine learning, data mining and modeling.', 'experience': '2+', 'expiry': '20/10/2023', 'id': '1006', 'loc': 'Redmond', 'postdate': '08/01/2019', 'salary': '100000', 'title': 'AI Engineer', 'type': 'Full time'}}), ('1007', {'Req': {'company': 'Apple', 'deadline': '01/03/2023', 'desc': 'The iOS Developer will be responsible for designing, developing and testing iOS applications. You will work closely with cross-functional teams to understand business needs, identify opportunities, and deliver high-quality solutions. The ideal candidate will have a background in computer science or a related field, and have experience in iOS development, Swift and Objective-C.', 'experience': '5+', 'expiry': '10/10/2023', 'id': '1007', 'loc': 'Redmond', 'postdate': '08/01/2019', 'salary': '100000', 'title': 'AI Engineer', 'type': 'Full time'}})])

    print('home func ran', jobdic)

    if request.method == 'POST' and request.POST.get('action') == 'first'  :
            #result = my_python_function()
            pass

    if 'clicked' in request.GET:
        if request.GET['clicked'] == 'xdfd':
            # do something
            print('yahoooo called function')
            pass
    return render(request, 'home.html', {
        'data' : jobdic
    })
def r_jobdetail(request):
    context = {}

    received_data= request.POST.get('getjobid_btn', None) # this is where we get the data when a request has been made even from a previous page/html
    print('received data, job detail page ran', received_data)

    # #uncomment these 3 lines to get proper response back
    try:
        id = received_data.split('¤¤¤')[0]
        title = received_data.split('¤¤¤')[1]
        desc = received_data.split('¤¤¤')[2]
        context['id'] = id
        context['title'] = title
        context['desc'] = desc
    except AttributeError:
        context['id'] = 'some id'
        context['title'] = 'some title'
        context['desc'] = '''<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p>At Nordic Solutions in Gothenburg, Sweden we work with some of Sweden’s largest automotive manufacturers within research and development. Now we are looking to expand our team of automotive software test engineers. Within the field of testing, the trend is moving towards automation. Therefore, we are looking for you who are an automotive software test engineer or automotive software developer, preferably experienced with Python and Continuous Integration (CI/CD). Here, we encourage and support our engineers to evolve professionally as personally. Therefore, you will have the fullest support from your closest Nordic Solutions manager, who will follow you in your journey and support you forward – in the direction you want. When you feel like you want to learn something new, you can always take it into your own hands because Nordic Solutions Academy offers several educations, from new programming languages to negotiation skills and much more.</p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p>To be successful in this role, we believe that you have:</p> <ul><li>Minimum 5 years of experience working with automotive software, either testing or development.</li> <li>Professional experience working with Python or C++.</li> <li>Worked in an Agile environment.</li> <li>A relevant degree in Computer Science, Software Engineering, Electronics, Data Science, Mathematics, Physics or similar.</li> </ul><p>Meritorious experience:</p> <ul><li>Experience in PyTest or Robot Framework.</li> <li>Experience with CI/CD tools e.g. Jenkins.</li> <li>Experience with Vector tools e.g. CANoe, CANalyzer.</li> <li>Experience with CAN, LIN, Ethernet.</li> </ul><p>&nbsp;To succeed in the role as a consultant at Nordic Solutions you need to be analytical, have a great sense for quality, a positive attitude and you need to be a team-player. If You find this as an interesting next step and would like to get in touch with us, don’t hesitate to send in your application.&nbsp;</p> <p><strong>About Nordic Solutions</strong></p> <p>Nordic Solutions is one of Europe’s largest technology and IT consulting companies with over 45,000 employees in over 30 countries. Our engineers carry out complex and highly technical projects throughout the value chain of the most prestigious companies in all sectors, such as Automotive, Telecom, Industry, Energy, Aerospace &amp; Defense and Life Science. In Sweden, we are over 1300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</p> <p>For the fourth year in a row, Nordic Solutions has been named one of Sweden's most attractive employers by Karriärföretagen 2023, an award for employers that offer unique career and development opportunities.</p> <p>Welcome to read more about us at&nbsp;<a href="#" target="_blank" rel="noreferrer noopener">Nordic Solutions.se</a></p> <p>We are looking forward to your application!</p>    </div>'''

    #data=db.child('Jobs').child('Job Detail').get(id).val()
    #print(data['desc'])
    print('apply page called' , context['id'])
    # if 'data' in request.GET:
    #     print('yes data is avail')
    # Context is the data that we need to send to the html while rendering
    return render(request, 'job_detail_pg.html',{
        'job_id' : context} )


def rfilldata(request):
    if request.method == 'GET':
        print(
            'refreshed')
        id = 'some,id'
        title = 'some,title '
        desc = 'some,desc'
    context = {}
    received_data= request.POST.get('getjobid_btn', None) # this is where we get the data when a request has been made even from a previous page/html
    print('r job detail page ran', received_data)
    try:
        id = received_data.split(',')[0]
        title = received_data.split(',')[1]
        context['id'] = id
        context['title'] = title
    except AttributeError:
        print('refreshed')
        id = 'Some Id'
        title = 'some title '
        desc = 'some desc'
        context['id'] = id
        context['title'] = title
    # Context is the data that we need to send to the html while rendering
    return render(request, 'applypage_html.html',{
        'job_id' : context} )


def applied(request):
    if request.method == 'POST':
        print('posttt', request.POST)
        #job_id = context['applybtn']
        a= request.POST['firstname_name']
        b= request.POST['lastname_name']
        c= request.POST['email_name']
        d= request.POST['phonenum_name']
        e= request.POST['coverletter_name']
        f= request.POST['exp_name']
        g= request.POST['eu_eligible_name']
        id = request.POST['submit_html']
        file = request.FILES.get('file_html')
        print('file', file)
        file_path = storage.child('files/' + file.name).put(file)
        print('filepath',file_path)
        #print(storage.child('files').put(file_cv))
        url = storage.child('files/' + file.name).get_url(token=None)
        print('url', url)
        datatopush= {'firstname_name': a ,'lastname_name':b ,'email_name':c, 'phonenum_name':d, 'coverletter_name':e, 'exp_name':f, 'eu_eligible_name':g , 'url_cv' : url}
        db.child('Jobs').child('Job Detail').child(id).child('Applicants').child(c.split('@')[0].replace('.','').replace('_', '')).set(datatopush)
    return render(request, 'apply_success.html')

def success(request):
    print('success called')
    return render(request, 'success.html')
