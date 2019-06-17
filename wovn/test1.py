# ANIMAL = 'Tiger'
# import Foo
#
# Foo::Bar.value1

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)


for el in lines:
    print(el, end=";")



# description
translate.json

This file is used for language swapping.

JavaScript request for JSON:
for getting the txt_vals:


const data = await fetch(`${api_server}/get-translate/${user_lang}`);
const result = data.json();
result.forEach(res => {
    console.log(res);
    // "hello world" if user_lang = 'en'
});


Server side (Node.js)
app.get(`${api_server}/get-translate/:user_lang`, async (req, res) => {
    const data = await DataModel.get('get-translate', user_lang); //DataModel handles the db interactions
    res.send(data);
})

SQL:
SELECT * from text_values where lang = ${user_lang}




Setting.json
this file is used for toggling between dynamic/statuc values by passing a boolean "dynamic_values"
the "hide_widget" used for hiding certain UI elements or widgets based on the boolean

JS:
const isDynamic = await fetch(${api_server}/settings/is_dynamic);
const result = await isDynamic.json();
if (result.dynamic_values) {
    //set dynamic value flag on html page
}
