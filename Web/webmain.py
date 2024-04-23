from flask import Flask, render_template, request
from Web.danchan_predict import danchan_predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 从表单中获取用户输入的地名和年份
        area = request.form['area']
        year = request.form['year']

        # 调用函数计算系数
        danchan = danchan_predict(area, year)

        # 渲染模板并将计算结果传递给模板
        return render_template('result.html', Y_t=danchan)
    else:
        # 如果是 GET 请求，返回 HTML 表单页面供用户输入地名和年份
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

