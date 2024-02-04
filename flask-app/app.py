from flask import Flask,render_template,request
from data import *
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app, resources={r"/process": {"origins": "http://localhost:3000"}})


def get_trained_tree():
    feature_train_data = pd.read_csv("./Data/feature_train.csv").iloc[:]
    label_train_data = pd.read_csv("./Data/label_train.csv").iloc[:]
    feature_test_data = pd.read_csv("./Data/feature_test.csv").iloc[:]
    label_test_data = pd.read_csv("./Data/label_test.csv").iloc[:]
    dataset_all = pd.read_csv("./Data/diabetes_012_health_indicators_BRFSS2015.csv")


    merged_train_files = label_train_data.merge(feature_train_data, how='outer', left_index=True, right_index=True)
    merged_test_files = label_test_data.merge(feature_test_data, how='outer', left_index=True, right_index=True)
    max_gain = max_gain_feature(merged_train_files.drop("Diabetes_012", axis=1), merged_train_files["Diabetes_012"])

    tree = Tree()
    tree.build(merged_train_files,max_gain)
    
    return tree


trained_tree = get_trained_tree()
result = ""

def convert_values_to_int(json_obj):
    return {key: int(value) if str(value).isnumeric() else value for key, value in json_obj.items()}

def result_of_predict(json_file):
    dataframe = pd.DataFrame([json_file])
    result = trained_tree.predict(dataframe)[0]
    if result==0:
        return "Fortunately, you don't have diabetes."
    elif result==1:
        return "Unfortunately, you have type 1 diabetes"
    elif result==2:
        return "Unfortunately, you have type 2 diabetes"

@app.route('/process', methods=['POST'])
def process_json():
    global result
    data = request.get_json()
    data = convert_values_to_int(data)
    dataframe = pd.DataFrame([data])
    result = result_of_predict(data)
    print(result)
    return jsonify({'result': result})

@app.route('/getresult', methods=['GET'])
def show_result():
    global result
    print(result)
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(debug=True,port=8080)
