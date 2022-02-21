@login_required
@permission_required("college.view_student", raise_exception=True)
def List_Student(request):
    Last_Semester = Semester.objects.all().order_by('-year').first()
    checked=request.POST.getlist('checks[]')
    student_uuid = request.POST.getlist('student_uuid')
    Student_List = ListStudent.objects.all()
    
    if checked:      
        filename = "Student_List.xlsx"
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        worksheet.set_paper('A4')
        # worksheet.repeat_rows(0, 7)
        worksheet.set_print_scale(75)
        worksheet.set_margins(left=0.5,right=0.5,top=0.5,bottom=0.5)

        maintitlecell = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 20})
        maintitlecell.set_text_wrap()

        subtitlecell = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 15})
        subtitlecell.set_text_wrap()

        centertitlecell = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 10})
        centertitlecell.set_text_wrap()

        centertitlecellborder = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 10})
        centertitlecellborder.set_text_wrap()

        lefttitlecell = workbook.add_format({
            'bold': 1,
            'align': 'left',
            'valign': 'vcenter',
            'font_size': 10})
        lefttitlecell.set_text_wrap()

        leftdatacell = workbook.add_format({
            'align': 'left',
            'valign': 'vcenter',
            'font_size': 10,})
        leftdatacell.set_text_wrap()

        leftdatacellborder = workbook.add_format({
            'border': 1,
            'align': 'left',
            'valign': 'vcenter',
            'font_size': 10,})
        leftdatacellborder.set_text_wrap()

        centerdatacell = workbook.add_format({
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 10})
        centerdatacell.set_text_wrap()

        Logo = os.path.join(settings.BASE_DIR, "static/assets/images/Logo", "College_Logo.png")
        worksheet.insert_image('A1',Logo, {'x_offset': 15, 'y_offset': 10,'x_scale': 1, 'y_scale': 0.8})
        worksheet.merge_range('B2:F2',str(SITE['Name']), maintitlecell)
        worksheet.merge_range('B3:F3',str(Last_Semester.year) + _('Student List'), subtitlecell)
        worksheet.merge_range('A4:F4', '', leftdatacell)
        worksheet.set_column('A:BE', 20)

        count=0
        col=["A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","K5","L5","M5","N5","O5","P5","Q5","R5","S5","T5","U5","V5","W5","X5","Y5","Z5","AA5","AB5","AC5","AD5","AE5","AF5","AG5","AH5","AI5","AJ5","AK5","AL5",'AM5',"AN5","AO5","AP5","AQ5","AR5","AS5","AT5","AU5","AV5","AW5","AX5","AY5","AZ5","BA5","BB5","BC5","BD5","BE5","BF5","BG5","BH5","BI5","BJ5","BK5","BL5"]
        if 'username_c' in checked:
            worksheet.write(col[0],  _('Username'), centertitlecell)
            count=count+1
        if 'name_c' in checked:
            worksheet.write(col[0+count],  _('Name'), centertitlecell)
            count=count+1
        if 'surname_c' in checked:
            worksheet.write(col[0+count],  _('Surname'), centertitlecell)
            count=count+1
        if 'std_no_c' in checked:
            worksheet.write(col[0+count],  _('Student Number'), centertitlecell)
            count=count+1
        if 'registration_classyear_c' in checked:
            worksheet.write(col[0+count],  _('Class Year'), centertitlecell)
            count=count+1  
        if 'std_cls_c' in checked:
            worksheet.write(col[0+count],  _('Class'), centertitlecell)
            count=count+1
        if 'idcard_c' in checked:
            worksheet.write(col[0+count],  _('ID Card Number'), centertitlecell)
            count=count+1
        if 'mother_c' in checked:
            worksheet.write(col[0+count],  _('Mother'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Mother') + ' ' +_('Birth Place'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Mother')+ ' ' +_('Birth Date'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count], _('Mother')+' '+_('Phone Mobile'), centertitlecell) 
            count=count+1
            worksheet.write(col[0+count],  _('Mother')+' '+_('Education'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Mother')+' '+_('Work'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Mother')+' '+_('Job'), centertitlecell)
            count=count+1
            
            worksheet.write(col[0+count],  _('Mother')+' '+_('E-mail'), centertitlecell)
            count=count+1
        if 'father_c' in checked :
            worksheet.write(col[0+count],  _('Father'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Father') + ' ' +_('Birth Place'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Father')+ ' ' +_('Birth Date'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Father')+' '+_('Phone Mobile'), centertitlecell) 
            count=count+1
            worksheet.write(col[0+count],  _('Father')+' '+_('Education'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Father')+' '+_('Work'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Father')+' '+_('Job'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Father')+' '+_('E-mail'), centertitlecell)
            count=count+1 
        if 'guardian_c' in checked:
            worksheet.write(col[0+count],  _('Guardian'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Guardian')+' '+_('Name')+' '+_('Surname'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Guardian')+' '+_('Phone Mobile'), centertitlecell) 
            count=count+1
            worksheet.write(col[0+count],  _('Guardian')+' '+_('Education'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Guardian')+' '+_('Work'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Guardian')+' '+_('Job'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Guardian')+' '+_('E-mail'), centertitlecell)
            count=count+1
        if 'bloodtype_c' in checked:
            worksheet.write(col[0+count],  _('Blood Type'), centertitlecell)
            count=count+1
        if 'gender_c' in checked:
            worksheet.write(col[0+count],  _('Gender'), centertitlecell)
            count=count+1
        if 'birthplace_c' in checked:
            worksheet.write(col[0+count],  _('Birth Place'), centertitlecell)
            count=count+1
        if 'birthdate_c' in checked:
            worksheet.write(col[0+count],  _('Birth Date'), centertitlecell)
            count=count+1
        if 'nationality_c' in checked:
            worksheet.write(col[0+count],  _('Nationality'), centertitlecell)
            count=count+1
        if 'region_c' in checked:
            worksheet.write(col[0+count],  _('Region'), centertitlecell)
            count=count+1
        if 'phone_home_c' in checked:
            worksheet.write(col[0+count],  _('Phone Home'), centertitlecell)
            count=count+1
        if 'phone_mobile_c' in checked:
            worksheet.write(col[0+count],  _('Phone Mobile'), centertitlecell)
            count=count+1
        if 'address_c' in checked:
            worksheet.write(col[0+count],  _('Address'), centertitlecell)
            count=count+1
        if 'parent_martial_status_c' in checked:
            worksheet.write(col[0+count],  _('Parents Are Married'), centertitlecell)
            count=count+1
        if 'mother_alive_c' in checked:
            worksheet.write(col[0+count],  _('Mother Alive'), centertitlecell)
            count=count+1
        if 'father_alive_c' in checked:
            worksheet.write(col[0+count],  _('Father Alive'), centertitlecell)
            count=count+1
        if 'divorced_mother_marital_status_c' in checked:
            worksheet.write(col[0+count],  _('Mother Married'), centertitlecell)
            count=count+1   
        if 'divorced_father_marital_status_c' in checked:
            worksheet.write(col[0+count],  _('Father Married'), centertitlecell)
            count=count+1 
        if 'with_whom_c' in checked:
            worksheet.write(col[0+count],  _('With Whom'), centertitlecell)
            count=count+1  
        if 'special_notes_c' in checked:
            worksheet.write(col[0+count],  _('General info'), centertitlecell)
            count=count+1 
        if 'health_notes_c' in checked:
            worksheet.write(col[0+count],  _('Healt info'), centertitlecell)
            count=count+1  
        if 'firstregistration_date_c' in checked:
            worksheet.write(col[0+count],  _('First Registration Date'), centertitlecell)
            count=count+1  
        if 'preregistration_date_c' in checked:
            worksheet.write(col[0+count],  _('PreRegistration Date'), centertitlecell)
            count=count+1  
        if 'preregistration_fee_c' in checked:
            worksheet.write(col[0+count],  _('Pre Registration Fee'), centertitlecell)
            count=count+1  
        if 'foreign_language_c' in checked:
            worksheet.write(col[0+count],  _('Foreign Language'), centertitlecell)
            count=count+1  
        if 'acceptance_type_c' in checked:
            worksheet.write(col[0+count],  _('Acceptance Type'), centertitlecell)
            count=count+1  
        if 'scholarship_c' in checked:
            worksheet.write(col[0+count],  _('Scholarship'), centertitlecell)
            count=count+1  
        if 'uniform_c' in checked:
            worksheet.write(col[0+count],  _('Free School Uniform'), centertitlecell)
            count=count+1  
        if 'food_c' in checked:
            worksheet.write(col[0+count],  _('Food'), centertitlecell)
            count=count+1  
        if 'service_c' in checked:
            worksheet.write(col[0+count],  _('Use Transfer'), centertitlecell)
            count=count+1  
            worksheet.write(col[0+count],  _('Root'), centertitlecell)
            count=count+1 
            worksheet.write(col[0+count],  _('Receive address'), centertitlecell)
            count=count+1 
            worksheet.write(col[0+count],  _('Region'), centertitlecell)
            count=count+1 
            worksheet.write(col[0+count],  _('Deliver Guard'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Deliver adress'), centertitlecell)
            count=count+1
            worksheet.write(col[0+count],  _('Region'), centertitlecell)
            count=count+1 
            worksheet.write(col[0+count],  _('Receive Guard'), centertitlecell)
            count=count+1
        if 'previous_school_c' in checked:
            worksheet.write(col[0+count],  _('Previous School'), centertitlecell)
            count=count+1
        row = 6
        if True:
            col_s=['A','B','C','D','E','F','G','H','I',"J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AL",'AM',"AN","AO","AP","AQ","AR","AS","AT","AU","AV","AW","AX","AY","AZ","BA","BB","BC","BD","BE","BF","BG","BH","BI","BJ","BK","BL"]
            count_s=0
            for preregistration in Student_List:
                count_s=0
                transfer = Transfer.objects.filter(semester=Last_Semester,student=preregistration.uuid).first()
                if 'username_c' in checked:
                    if preregistration.user:
                        worksheet.write(col_s[0]+str(row),preregistration.user, centerdatacell)
                    else:
                        worksheet.write(col_s[0]+str(row),'', centerdatacell)
                    count_s=count_s+1  
                if 'name_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.name, leftdatacellborder)
                    count_s=count_s+1
                if 'surname_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.surname, leftdatacellborder)
                    count_s=count_s+1
                if 'std_no_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.std_no, leftdatacellborder)
                    count_s=count_s+1
                if 'registration_classyear_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.registration_classyear, centerdatacell)
                    count_s=count_s+1
                if 'std_cls_c' in checked:
                    if str(preregistration.class_year) > "8":
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.class_year)+''+str(preregistration.class_name)+' '+str(preregistration.class_branch), centerdatacell)
                    else:
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.class_year)+''+str(preregistration.class_name), centerdatacell)
                    count_s=count_s+1
                if 'idcard_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.id_no, centerdatacell)
                    count_s=count_s+1
                if 'mother_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_name), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_birthplace), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_birthdate.strftime('%d-%m-%Y')), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_phone_mobile), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(EDUCATIONS[preregistration.mother_education-1][1]), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_job), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_work), centerdatacell)
                    count_s=count_s+1
                    
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_email), centerdatacell)
                    count_s=count_s+1                    
                if 'father_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_name), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_birthplace), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_birthdate.strftime('%d-%m-%Y')), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_phone_mobile), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(EDUCATIONS[preregistration.father_education-1][1]), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_job), centerdatacell)
                    count_s=count_s+1
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_work), centerdatacell)
                    count_s=count_s+1
                    
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_email), centerdatacell)
                    count_s=count_s+1
                if 'guardian_c' in checked:
                    if preregistration.guardian ==  'M' and 'mother_c'  in checked:
                        worksheet.write(col_s[0+count_s]+str(row),str(_('Mother')), centerdatacell)
                        count_s=count_s+1
                        for space in range(1,7):
                            worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                            count_s=count_s+1
                            mothercheck =True 
                    elif preregistration.guardian ==  'F' and 'father_c'  in checked:
                        worksheet.write(col_s[0+count_s]+str(row),str(_('Father')), centerdatacell)
                        count_s=count_s+1
                        for space in range(1,7):
                            worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                            count_s=count_s+1 
                            fathercheck=True
                    if preregistration.guardian ==  'O':
                        worksheet.write(col_s[0+count_s]+str(row),str(_('Other')), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.other_name), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.other_phone_mobile), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(EDUCATIONS[preregistration.other_education-1][1]), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.other_job), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.other_work), centerdatacell)
                        count_s=count_s+1
                        
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.other_email), centerdatacell)
                        count_s=count_s+1
                    elif preregistration.guardian ==  'M' and 'mother_c' not in checked:

                        worksheet.write(col_s[0+count_s]+str(row),str(_('Mother')), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_name), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_phone_mobile), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(EDUCATIONS[preregistration.mother_education-1][1]), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_work), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_job), centerdatacell)
                        count_s=count_s+1
                        
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.mother_email), centerdatacell)
                        count_s=count_s+1
                    elif preregistration.guardian ==  'F' and 'father_c' not in checked:
                        worksheet.write(col_s[0+count_s]+str(row),str(_('Father')), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_name), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_phone_mobile), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(EDUCATIONS[preregistration.father_education-1][1]), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_work), centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_job), centerdatacell)
                        count_s=count_s+1
                        
                        worksheet.write(col_s[0+count_s]+str(row),str(preregistration.father_email), centerdatacell)
                        count_s=count_s+1
                if 'bloodtype_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row), preregistration.blood_type, centerdatacell)
                    count_s=count_s+1
                if 'gender_c' in checked:
                    for gender in GENDERS:
                        if preregistration.gender == gender[0]:
                            worksheet.write(col_s[0+count_s]+str(row),str(gender[1]), centerdatacell)
                    count_s=count_s+1
                if 'birthplace_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.birthplace, centerdatacell)
                    count_s=count_s+1
                if 'birthdate_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.birthdate.strftime('%d-%m-%Y'), centerdatacell)
                    count_s=count_s+1
                if 'nationality_c' in checked:
                    if translation.get_language()=='tr' :
                        worksheet.write(col_s[0+count_s]+str(row) ,str(preregistration.nationality_local_name), centerdatacell)
                    else:
                        worksheet.write(col_s[0+count_s]+str(row) ,str(preregistration.nationality_foreign_name), centerdatacell)
                    count_s=count_s+1
                if 'region_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),str(preregistration.region_name), centerdatacell)
                    count_s=count_s+1
                if 'phone_home_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.phone_home, centerdatacell)
                    count_s=count_s+1
                if 'phone_mobile_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.phone_mobile, centerdatacell)
                    count_s=count_s+1
                if 'address_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.address, leftdatacellborder)
                    count_s=count_s+1
                if 'parent_martial_status_c' in checked:
                    for martial_status in MARTIAL_STATUS:
                        if preregistration.parent_martial_status == martial_status[0]:
                            worksheet.write(col_s[0+count_s]+str(row) ,str(martial_status[1]), centerdatacell)
                    count_s=count_s+1
                if 'mother_alive_c' in checked:
                    for parent_alive in PARENT_ALIVE:
                        if preregistration.mother_alive == parent_alive[0]:
                            worksheet.write(col_s[0+count_s]+str(row) ,str(parent_alive[1]), centerdatacell)
                    count_s=count_s+1
                if 'father_alive_c' in checked:
                    for parent_alive in PARENT_ALIVE:
                        if preregistration.father_alive == parent_alive[0]:
                            worksheet.write(col_s[0+count_s]+str(row) ,str(parent_alive[1]), centerdatacell)
                    count_s=count_s+1
                if 'divorced_mother_marital_status_c' in checked:
                    if not preregistration.parent_martial_status and preregistration.divorced_mother_marital_status:
                        worksheet.write(col_s[0+count_s]+str(row),_('Yes'), centerdatacell)
                    elif not preregistration.parent_martial_status and not preregistration.divorced_mother_marital_status:
                        worksheet.write(col_s[0+count_s]+str(row),_('No'), centerdatacell)
                    else:
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                    count_s=count_s+1
                if 'divorced_father_marital_status_c' in checked:
                    if not preregistration.parent_martial_status and preregistration.divorced_father_marital_status:
                        worksheet.write(col_s[0+count_s]+str(row),_('Yes'), centerdatacell)
                    elif not preregistration.parent_martial_status and not preregistration.divorced_father_marital_status:
                        worksheet.write(col_s[0+count_s]+str(row),_('No'), centerdatacell)
                    else:
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                    count_s=count_s+1
                if 'with_whom_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.with_whom, leftdatacellborder)
                    count_s=count_s+1
                if 'special_notes_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.special_notes, leftdatacellborder)
                    count_s=count_s+1
                if 'health_notes_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.health_notes, leftdatacellborder)
                    count_s=count_s+1
                if 'firstregistration_date_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.preregistration_date.strftime('%d-%m-%Y'), centerdatacell)
                    count_s=count_s+1
                if 'preregistration_date_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.preregistration_date.strftime('%d-%m-%Y'), centerdatacell)
                    count_s=count_s+1
                if 'preregistration_fee_c' in checked:
                    worksheet.write(col_s[0+count_s]+str(row),preregistration.preregistration_fee, centerdatacell)
                    count_s=count_s+1
                if 'foreign_language_c' in checked:
                    if translation.get_language()=='en' :
                        worksheet.write(col_s[0+count_s]+str(row),preregistration.foreign_language, centerdatacell)
                    elif translation.get_language()=='tr' :
                        worksheet.write(col_s[0+count_s]+str(row),preregistration.local_language, centerdatacell)
                    count_s=count_s+1
                if 'acceptance_type_c' in checked:
                    if translation.get_language()=='en' :
                        worksheet.write(col_s[0+count_s]+str(row),preregistration.acceptance_foreign_name, centerdatacell)
                    elif translation.get_language()=='tr' :
                        worksheet.write(col_s[0+count_s]+str(row),preregistration.acceptance_local_name, centerdatacell)
                    count_s=count_s+1
                if 'scholarship_c' in checked:
                    for scholarship in SCHOLARSHIP_TYPES:
                        if preregistration.scholarship == scholarship[0]:
                            worksheet.write(col_s[0+count_s]+str(row) ,str(scholarship[1]), leftdatacellborder)
                    count_s=count_s+1
                if 'uniform_c' in checked:
                    if preregistration.uniform:
                        worksheet.write(col_s[0+count_s]+str(row),_('Yes'), centerdatacell)
                    else:
                        worksheet.write(col_s[0+count_s]+str(row),_('No'), centerdatacell)
                    count_s=count_s+1
                if 'food_c' in checked:
                    if preregistration.food:
                        worksheet.write(col_s[0+count_s]+str(row),_('Yes'), centerdatacell)
                    else:
                        worksheet.write(col_s[0+count_s]+str(row),_('No'), centerdatacell)
                    count_s=count_s+1
                if 'service_c' in checked:
                    if preregistration.transfer:
                        worksheet.write(col_s[0+count_s]+str(row),_('Yes'), centerdatacell)
                        count_s=count_s+1
                        if transfer.root:
                            worksheet.write(col_s[0+count_s]+str(row),str(TRANSFER_ROOT[transfer.root - 1][1]), centerdatacell)
                            count_s=count_s+1
                            if transfer.root==1:
                                worksheet.write(col_s[0+count_s]+str(row),transfer.goingaddress , centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),str(transfer.deliver_guard1_name)+' '+str(transfer.deliver_guard1_surname)+' ('+str(transfer.deliver_guard1_phone)+')', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),transfer.going_region.name, centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                            elif transfer.root==2:    
                                worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),transfer.backaddress, centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),transfer.back_region.name, centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),str(transfer.receive_guard1_name)+' '+str(transfer.receive_guard1_surname)+' '+str(transfer.receive_guard1_phone), centerdatacell)
                                count_s=count_s+1    
                            elif transfer.root==3:    
                                worksheet.write(col_s[0+count_s]+str(row),transfer.goingaddress , centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),transfer.going_region.name, centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),str(transfer.deliver_guard1_name)+' '+str(transfer.deliver_guard1_surname)+' ('+str(transfer.deliver_guard1_phone)+')', centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),transfer.backaddress, centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),transfer.back_region.name, centerdatacell)
                                count_s=count_s+1
                                worksheet.write(col_s[0+count_s]+str(row),str(transfer.receive_guard1_name)+' '+str(transfer.receive_guard1_surname)+' '+str(transfer.receive_guard1_phone), centerdatacell)
                                count_s=count_s+1
                    else:
                        worksheet.write(col_s[0+count_s]+str(row),_('No'), centerdatacell)
                        count_s=count_s+1 
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),str(transfer.guard1_name)+' '+str(transfer.guard1_surname)+' ('+str(transfer.guard1_phone)+') ', centerdatacell)
                        count_s=count_s+1
                        worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                        count_s=count_s+1
                        if transfer.guard2_name:
                             worksheet.write(col_s[0+count_s]+str(row),str(transfer.guard2_name)+' '+str(transfer.guard2_surname)+' ('+str(transfer.guard2_phone)+') ', centerdatacell)
                        else:
                            worksheet.write(col_s[0+count_s]+str(row),'', centerdatacell)
                if 'previous_school_c' in checked:
                    if preregistration.previous_school == 104:
                        worksheet.write(col_s[0+count_s]+str(row) ,str(preregistration.other_previous_school), centerdatacell)
                    else:
                        for KKTC_SCHOOL in KKTC_SCHOOL_LIST:
                            if preregistration.previous_school == KKTC_SCHOOL[0]:
                                worksheet.write(col_s[0+count_s]+str(row) ,str(KKTC_SCHOOL[1]), centerdatacell)
                    count_s=count_s+1

                row +=1


        workbook.close()
        with open(filename, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
            os.remove(filename)
            return response

    return render(request, 'List-Student.html',{'Student_List':Student_List,
                                                'STATUS_LIST':STD_STATUS,
                                                'SCHOLARSHIP_LIST':SCHOLARSHIP_TYPES,
                                                'CLASS_YEAR_LIST':CLASS_YEARS,
                                                'BLOOD_TYPE_LIST':BLOOD_TYPES,
                                                'GUARDIAN_TYPE_LIST':GUARDIAN_TYPES,
                                                'EDUCATION_LIST':EDUCATIONS,
                                                'GENDER_LIST':GENDERS,
                                                'MARTIAL_STATUS_LIST':MARTIAL_STATUS,
                                                'PARENT_ALIVE_LIST':PARENT_ALIVE,
                                                'KKTC_SCHOOL_LIST':KKTC_SCHOOL_LIST,})