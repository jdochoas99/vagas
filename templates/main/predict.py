from prediction import mkprediction

with open('../../templates/main/teste.html','w') as t:
    a = mkprediction()
    t.write('{% block rect %}')
    for _ in a:
        if _[1] == 1:
            t.write(f'<rect x=" {_[0][0]} " y="{_[0][1]}" style="fill:rgb(255, 0, 0)" opacity="1" width="40" height="90" />')
        else:
            t.write(f'<rect x=" {_[0][0]} " y=" {_[0][1]}" style="fill:rgb(255, 0, 0)" opacity="1" width="40" height="90" />')
    t.write(' {% endblock rect %}')


