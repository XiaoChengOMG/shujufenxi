from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import cx_Oracle
from mysite.models import CkKpdHz
#from django.views.decorators.csrf import csrf_exempt 
def login1(request):
	return render_to_response('login.html')

#@csrf_exempt
def login(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
	else:
		form = ContactForm()
	return render_to_response('login.html',{'r':form})



def index(request):
	now = datetime.datetime.now()
	list_s = []
	list_a = []
	conn = cx_Oracle.connect('lmis/lmis@LMIS_252')
	curs = conn.cursor()
	sql = "SELECT trunc(t.RIQI_DATE,'mm'),count(1) FROM viw_ck_kpd_hz t group by trunc(t.RIQI_DATE,'mm') ORDER BY trunc(t.RIQI_DATE,'mm') ASC"
	rr = curs.execute(sql)
	row = curs.fetchall()
	row = list(row)
	for i in row:
		list_s.append(i[0].strftime('%y%m'))#-%y %H:%M:%S
		list_a.append(i[1])
	return render_to_response('index.html',{'current_datetime':now,'list_s':list_s,'list_a':list_a,'row':row})

def xsck(request):
	l = CkKpdHz.objects.all()[0]
	return render_to_response('xsck.html',{'dj':l})