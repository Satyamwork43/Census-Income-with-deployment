 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open("/content/classifier1.pkl", "rb") 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age,Workclass,Fnlwgt,Education,Education_num,Marital_status,Occupation,Relationship,Race,Sex,Capital_gain,Capital_loss,Hours_per_week,Native_country):
     
 
    # Pre-processing user input    
    if Workclass == " Self-emp-not-inc":
        Workclass = 5
    elif Workclass == " Private":
        Workclass = 3
    elif Workclass == " State-gov":
        Workclass = 6
    elif Workclass == " Federal-gov":
        Workclass = 0
    elif Workclass == " Local-gov":
        Workclass = 1
    elif Workclass == " Unknown":
        Workclass = 8
    elif Workclass == " Self-emp-inc":
        Workclass = 4
    elif Workclass == " Without-pay":
        Workclass = 7
    elif Workclass == " Never-worked":
      Workclass = 2
    
    
    if Education == " Bachelors":
      Education = 9
    elif Education == " HS-grad":
      Education = 11 
    elif Education == " 11th":
      Education = 1
    elif Education == " Masters":
      Education = 12
    elif Education == " 9th":
      Education = 6
    elif Education == " Some-college":
      Education = 15
    elif Education == " Assoc-acdm":
      Education = 7
    elif Education == " Assoc-voc":
      Education = 8
    elif Education == " 7th-8th":
      Education = 5
    elif Education == " Doctorate":
      Education = 10
    elif Education == " Prof-school":
      Education = 14
    elif Education == " 5th-6th":
      Education = 4
    elif Education == " 10th":
      Education = 0
    elif Education == " 1st-4th":
      Education = 3
    elif Education == " 12th":
      Education = 2
    elif Education == " Preschool":
      Education = 13

    if Sex == "Male":
      Sex = 1
    elif Sex == "Female":
      Sex = 0

    if Marital_status == ' Married-civ-spouse':
      Marital_status = 2
    elif Marital_status == ' Divorced':
      Marital_status = 0
    elif Marital_status == ' Married-spouse-absent':
      Marital_status = 3
    elif Marital_status == ' Never-married':
      Marital_status = 4
    elif Marital_status == ' Separated':
      Marital_status = 5
    elif Marital_status == ' Married-AF-spouse':
      Marital_status = 1
    elif Marital_status == ' Widowed':
      Marital_status = 6


    if Occupation == ' Exec-managerial':
      Occupation = 4
    elif Occupation == ' Handlers-cleaners':
      Occupation = 6
    elif Occupation == ' Prof-specialty':
      Occupation = 10
    elif Occupation == ' Other-service':
      Occupation = 8
    elif Occupation == ' Adm-clerical':
      Occupation = 1
    elif Occupation == ' Sales':
      Occupation = 12
    elif Occupation == ' Craft-repair':
      Occupation = 3
    elif Occupation == ' Transport-moving':
      Occupation = 14
    elif Occupation == ' Farming-fishing':
      Occupation = 5
    elif Occupation == ' Machine-op-inspct':
      Occupation = 7
    elif Occupation == ' Tech-support':
      Occupation = 13
    elif Occupation == ' ?':
      Occupation = 0
    elif Occupation == ' Protective-serv':
      Occupation = 11
    elif Occupation == ' Armed-Forces':
      Occupation = 2
    elif Occupation == ' Priv-house-serv':
      Occupation = 9
    
    if Relationship == ' Husband':
      Relationship = 0
    elif Relationship == ' Not-in-family':
      Relationship = 1
    elif Relationship == ' Wife':
      Relationship = 5
    elif Relationship == ' Own-child':
      Relationship = 3
    elif Relationship == ' Unmarried':
      Relationship = 4
    elif Relationship == ' Other-relative':
      Relationship = 2
    if Race == ' White':
      Race = 0
    elif Race == ' Black':
      Race = 1
    elif Race == ' Asian-Pac-Islander':
      Race = 2
    elif Race == ' Amer-Indian-Eskimo':
      Race = 3
    elif Race == ' Other':
      Race = 4

    if Sex == ' Male':
      Sex = 1
    elif Sex == ' Female':
      Sex = 0

    if Native_country == ' United-States':
      Native_country = 39
    elif Native_country == ' Cuba':
      Native_country = 5
    elif Native_country == ' Jamaica':
      Native_country = 23
    elif Native_country == ' India':
      Native_country = 19
    elif Native_country == ' ?':
      Native_country = 0
    elif Native_country == ' Mexico':
      Native_country = 26
    elif Native_country == ' South':
      Native_country = 35
    elif Native_country == ' Puerto-Rico':
      Native_country = 33
    elif Native_country == ' Honduras':
      Native_country = 16
    elif Native_country == ' England':
      Native_country = 9
    elif Native_country == ' Canada':
      Native_country = 2
    elif Native_country == ' Germany':
      Native_country = 11
    elif Native_country == ' Iran':
      Native_country = 20
    elif Native_country == ' Philippines':
      Native_country = 30
    elif Native_country == ' Italy':
      Native_country = 22
    elif Native_country == ' Poland':
      Native_country = 31
    elif Native_country == ' Columbia':
      Native_country = 4
    elif Native_country == ' Cambodia':
      Native_country = 1
    elif Native_country == ' Thailand':
      Native_country = 37
    elif Native_country == ' Ecuador':
      Native_country = 7
    elif Native_country == ' Laos':
      Native_country = 25
    elif Native_country == ' Taiwan':
      Native_country = 36
    elif Native_country == ' Haiti':
      Native_country = 14
    elif Native_country == ' Portugal':
      Native_country = 32
    elif Native_country == ' Dominican-Republic':
      Native_country = 6
    elif Native_country == ' El-Salvador':
      Native_country = 8
    elif Native_country == ' France':
      Native_country = 10
    elif Native_country == ' Guatemala':
      Native_country = 13
    elif Native_country == ' China':
      Native_country = 3
    elif Native_country == ' Japan':
      Native_country = 24
    elif Native_country == ' Yugoslavia':
      Native_country = 41
    elif Native_country == ' Peru':
      Native_country = 29
    elif Native_country == ' Outlying-US(Guam-USVI-etc)':
      Native_country = 28
    elif Native_country == ' Scotland':
      Native_country = 34
    elif Native_country == ' Trinadad&Tobago':
      Native_country = 38
    elif Native_country == ' Greece':
      Native_country = 12
    elif Native_country == ' Nicaragua':
      Native_country = 27
    elif Native_country == ' Vietnam':
      Native_country = 40
    elif Native_country == ' Hong':
      Native_country = 17
    elif Native_country == ' Ireland':
      Native_country = 21
    elif Native_country == ' Hungary':
      Native_country = 18
    elif Native_country == ' Holand-Netherlands':
      Native_country = 15
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Age,Workclass,Fnlwgt,Education,Education_num,Marital_status,Occupation,Relationship,Race,Sex,Capital_gain,Capital_loss,Hours_per_week,Native_country]])
     
    if prediction == 1:
      pred = ">50k"
    else:
      pred = "<=50k"
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:red;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Census Income Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Workclass = st.selectbox("Workclass",(' Self-emp-not-inc', ' Private', ' State-gov', ' Federal-gov',
       ' Local-gov', ' ?', ' Self-emp-inc', ' Without-pay',
       ' Never-worked'))
    Education = st.selectbox("Education",(' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th',
       ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th',
       ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th', ' 1st-4th',
       ' Preschool', ' 12th')) 
    Age	 = st.number_input("Age")

    Marital_status = st.selectbox("Marital_status",(' Married-civ-spouse', ' Divorced', ' Married-spouse-absent',
       ' Never-married', ' Separated', ' Married-AF-spouse', ' Widowed'))
    Occupation = st.selectbox("Occupation",(' Exec-managerial', ' Handlers-cleaners', ' Prof-specialty',
       ' Other-service', ' Adm-clerical', ' Sales', ' Craft-repair',
       ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
       ' Tech-support', ' ?', ' Protective-serv', ' Armed-Forces',
       ' Priv-house-serv'))
    Race=st.selectbox("Race",(' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo',
       ' Other'))
    Sex=st.radio("Sex",(' Male', ' Female'))

    Relationship = st.selectbox("Relationship",(' Husband', ' Not-in-family', ' Wife', ' Own-child', ' Unmarried',
       ' Other-relative'))
    Native_country=st.selectbox("Native_country",(' United-States', ' Cuba', ' Jamaica', ' India', ' ?', ' Mexico',
       ' South', ' Puerto-Rico', ' Honduras', ' England', ' Canada',
       ' Germany', ' Iran', ' Philippines', ' Italy', ' Poland',
       ' Columbia', ' Cambodia', ' Thailand', ' Ecuador', ' Laos',
       ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',
       ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan',
       ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland',
       ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong',
       ' Ireland', ' Hungary', ' Holand-Netherlands'))
    Fnlwgt	= st.number_input("Fnlwgt [Range should be between 12285-1484705]")
    Education_num		= st.number_input("Education_num [Range should be Between 1-16]")
    Capital_gain	= st.number_input("Capital_gain [Range Should be Between 0-99999]")
    Capital_loss	= st.number_input("Capital_loss [Range Should be Between 0-4356]")
    Hours_per_week	= st.number_input("Hours_per_week [Range Should Be Between 1-99]")
   
    result =""
      
    # when "Predict" is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age,Workclass,Fnlwgt,Education,Education_num,Marital_status,Occupation,Relationship,Race,Sex,Capital_gain,Capital_loss,Hours_per_week,Native_country) 
        st.success("Your Income is {}".format(result))
     
if __name__=="__main__": 
    main()
