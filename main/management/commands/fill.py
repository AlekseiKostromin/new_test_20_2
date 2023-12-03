from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Петров', 'first_name': 'Николай'},
            {'last_name': 'Костромин', 'first_name': 'Алексей'},
            {'last_name': 'Долгополова', 'first_name': 'Ольга'},
            {'last_name': 'Елисеев', 'first_name': 'Дмитрий'},
            {'last_name': 'Сизов', 'first_name': 'Виктор'},
        ]
        #for student_item in student_list:
        #    Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item))

        Student.objects.bulk_create(students_for_create) # пакетный инсёрт

