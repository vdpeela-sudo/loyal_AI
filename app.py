import streamlit as st
import tensorflow as tf
import numpy as np

# యాప్‌కి పేరు పెడదాం!
st.title("లోయల్ AI - నా సొంత క్రియేషన్")

st.write("ఈ AI ని నేనే సొంతంగా కోడింగ్ చేసి ట్రైన్ చేసాను. ఇక్కడ కింద ఒక నెంబర్ ఇవ్వండి, దాన్ని 10 తో గుణించి AI ఎలా ఆన్సర్ చేస్తుందో చూడండి!")

# నెంబర్ ఎంటర్ చేయడానికి బాక్స్
user_input = st.number_input("ఏదైనా ఒక నెంబర్ ఇవ్వండి (ఉదాహరణకు: 15):", value=1.0)

if st.button("అంచనా వేయి (Predict)"):
    try:
        # మనం అప్‌లోడ్ చేసిన AI ఫైల్‌ని తీసుకుంటున్నాం
        model = tf.keras.models.load_model('my_first_ai_model.keras')
        
        # ఆన్సర్ కనుక్కుంటున్నాం
        prediction = model.predict(np.array([[user_input]]))
        result = round(prediction[0][0], 2)
        
        st.success(f"లోయల్ AI చెప్పిన ఆన్సర్: {result}")
    except Exception as e:
         st.error(f"ఏదో తప్పు జరిగింది. ఫైల్ పేరు కరెక్ట్‌గా ఉందో లేదో చూడండి. Error: {e}")
      
