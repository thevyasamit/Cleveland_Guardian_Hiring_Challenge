from flask import *
import json

app = Flask(__name__)

@app.route("/", methods =['GET','POST'])
def home():
    deptList = []
    deptemp = []
    returnData = []
    empIds = []
    msg = ''
    flag = 0
    with open("Employees.json", "r") as employees_file:
        employees = json.load(employees_file)
    
    with open("Requests.json", "r") as requests_file:
        requests = json.load(requests_file)
            
    if request.method == 'POST':

        if request.form['empid'] != '':
            empid = request.form['empid']
            for i in range(0,len(employees)):
                if employees[i]['employee_id'] == int(empid) and employees[i]['isAdmin'] == 'yes':
                    flag = 1
                    break
            if flag == 1:
                for i in range(0, len(requests)):
                    msg = '!!!!!  ADMIN  !!!!!!'
                    returnData.append(requests[i])
            else:

                for i in range(0, len(requests)):
                    if requests[i]['employee_id'] == int(empid):
                        returnData.append(requests[i])
                


        elif 'dept' in request.form:
            dept = request.form['dept'].lower()
            for i in range(0, len(employees)):
                if employees[i]['department'].lower() == dept:
                    deptemp.append(int(employees[i]['employee_id']))
            for i in range(0, len(requests)):
                if requests[i]['employee_id'] in deptemp:
                    returnData.append(requests[i])

    return render_template("home.html", msg = msg, data=returnData)

        
if __name__ == "__main__":
    app.run()