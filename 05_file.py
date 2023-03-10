open_file=open('point.txt')
data=open_file.read()
open_file.close()
point_data=data.splitlines()

point_dict={}
for line in point_data:
    student_name,points_str=line.split(":")
    point_dict[student_name]=points_str

score_dict={}
for syudent_name in point_dict:
    point_list=point_dict[student_name].split(":")
    subject_number=len(point_list)
    total=0

for point in point_list:
    total+=int(point)

average=total/subject_number
score_dict[subject_name]=(total,average,subject_number)

evaliation_dict={}
for student_name in score_dict:
    score_data=score_dict[student_name]
    total=score_data[0]
    average=score_data[1]
    subject_number=score_data[2]

excellent=subject_number*100*0.8
good=subject_number*100*0.65
if total>=excellent:
    evaluation="Excellent"
elif total>=good:
    evaluation="good"
else:
    evaluation="Bad"

evaluation_dict[student_name]=evaluation

file_name="evaluation.txt"
output_file=open(file_name,"w")
for student_name in score_dict:
    score_data=score_dict[student_name]
    total=score_data[0]

    evaluation=evaluation_dict[student_name]

text=f"[{student_name}]total:{total},evaluation:{evaluation}\n"
output_file.write(text)

output_file.close()
print(f"評価結果を{file_namw}に出力。")
