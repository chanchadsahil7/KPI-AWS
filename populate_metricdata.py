#populate_metricdata.py

import os, django, csv, datetime, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KPI_project.settings' )
django.setup()

from kpi_app.models import *

def populate():
	subjects_list, students_list = list(), list()
	x = list()
	company_obj = Company.objects.get(id=1)
	attr_obj = Attribute.objects.get(id=1)
	attr_1 = AttributeValue.objects.filter(attr_type_id=attr_obj.id)
	#print(attr_1[0])
	#exam_types = {'type of exam': [month for even sem, month for odd sem, minimum marks, maximum marks]}
	exam_types = {attr_1[0]: [2, 8, 15, 40], attr_1[1]: [4, 10, 25, 60], attr_1[2]: [6, 12, 35, 100]}
	semester = {'Sem I': 2014, 'Sem II': 2014, 'Sem III': 2015, 'Sem IV': 2015, 'Sem V': 2016, 'Sem VI': 2016}
	#for x in exam_types:
	#	print(x)

	attr_obj = Attribute.objects.get(id=2)
	students_list = AttributeValue.objects.filter(attr_type_id=attr_obj.id)
	#print(students_list[0])



	metric_obj = Metric.objects.get(id=1)

	bca_obj = DimensionValue.objects.filter(dim_name='BCA')[0]
	semesters = DimensionValue.objects.filter(parent=bca_obj)
	sem_index = 0

	for sem in semesters:
		print(sem.dim_name)
		exam_year = semester[sem.dim_name]
		print(exam_year)
		subjects = DimensionValue.objects.filter(parent=sem)
		sem_index += 1
		exam_day = 0

		for subject in subjects:
			print("\t", subject.dim_name)
			exam_day += 1

			for exam_type in exam_types.keys():
				exam_month = exam_types[exam_type][sem_index % 2]
				#print(exam_month)
				exam_date = datetime.date(exam_year, exam_month, exam_day)
				print("\t\t", exam_type, exam_date)
				min1 = exam_types[exam_type][2]
				print(min1)
				max1 = exam_types[exam_type][3]
				print(max1)


				for student in students_list:
					#print("\t\t\t", student['StudentName'])
					num = random.randrange(min1, max1)
					
					m = MetricData.objects.get_or_create(dim_1=subject, attr_1=student,
						attr_2= exam_type,
						date_associated=exam_date, metric_id=metric_obj,
						numerator=num, denominator=max1, company_name=company_obj)[0]
					m.save()
					print(student," created")

if __name__ == '__main__':
	print("Starting to populate data")
	populate()
