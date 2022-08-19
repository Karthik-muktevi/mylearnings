from flask import Flask,render_template,request
import re

app = Flask(__name__)

@app.route('/search',methods=['GET','POST'])
def regex():

    if request.method =='POST':
        regular_expression = request.form[r'in_1']
        text_string = request.form['in_2']



        match =[i for i in re.findall(regular_expression, text_string)]
        start_index = [j.start() for j in
         re.finditer(regular_expression, text_string)]
        end_index = [j.end() for j in
         re.finditer(regular_expression, text_string)]
        span = [i.span() for i in re.finditer(regular_expression, text_string)]



        return render_template('result.html',match=match,start_index=start_index,end_index=end_index,span=span)
        if len(match) == 0:
            print('Match not found')
            return render_template('index.html')
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)