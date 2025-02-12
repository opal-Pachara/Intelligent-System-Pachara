import streamlit as st
from PIL import Image
# import pickle
# import torch
import numpy as np
import base64

def main():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Athiti:wght@400&display=swap');

html, body, [class*="css"] {
    font-family: 'Athiti', sans-serif;
    font-size: 16px; /* ปรับขนาดให้เหมาะสม */
    font-weight: 400; /* ใช้ Regular */
    line-height: 1.6; /* เพิ่มระยะห่างระหว่างบรรทัด */
    color: #ffffff; /* สีขาว */
    background-color: #121212; /* พื้นหลังสีดำ (หรือเปลี่ยนตามต้องการ) */
}

.stSidebar, .stRadio, .stButton>button, .stMarkdown, 
.stTextInput, .stNumberInput {
    font-family: 'Athiti', sans-serif !important;
    font-size: 16px !important;
    font-weight: 400 !important;
    line-height: 1.6 !important;
    color: #ffffff !important; /* ทำให้สีขาว */
}
        @media (prefers-color-scheme: dark) {
            .stApp {
                background: #121212; 
                color: white;
            }
            h1, h2, h3, h4 {
                color: #B0B0B0; /* เทาอ่อน */
            }
            .stButton>button {
                background-color: #333333;
                color: white;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #555555;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #555555;
            }
            .stTextInput>div>div>input {
                background-color: #222222;
                color: white;
                border: 1px solid #444444;
            }
        }

        @media (prefers-color-scheme: light) {
            .stApp {
                background: white;
                color: black;
            }
            h1, h2, h3, h4 {
                color: #333333;
            }
            .stButton>button {
                background-color: #E0E0E0;
                color: black;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #BBBBBB;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #CCCCCC;
            }
            .stTextInput>div>div>input {
                background-color: #F0F0F0;
                color: black;
                border: 1px solid #CCCCCC;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    st.logo("img/logo.png",size="large")
    st.sidebar.title("Intelligent System Project")
    st.sidebar.caption("Phatchara Worrawat 6404062610324")
    st.sidebar.title("Menu")
    page = st.sidebar.radio("", ["Introduction & Data Set", "Algorithm & Model Development", "Machine Learing Model", "Neural Network Model"])

    if page == "Introduction & Data Set":
        show_introduction()
    elif page == "Algorithm & Model Development":
        show_model_development()
    elif page == "Machine Learing Model":
        show_ml_demo()
    elif page == "Neural Network Model":
        show_nn_demo()

def show_introduction():
    st.markdown("""<h1 style='font-family: Athiti; text-align: center;'>Introduction & Data Set</h1>""", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Introduction",
    "What is AI ML DL",
    "Why Data Prepare for Training",
    "Data Set Sources",
    "Machine Learning",
    "Neural Network"
])
    # tab1, tab2 ,tab3 ,tab4 ,tab5, tab6= st.tabs(["Introduction","What is AI,ML,DL ?","Why prepare data for training ML/AI?", "Source of Data Set","Machine Learning","Neural Network"])
    with tab1:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Introduction☺️
    </h4>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    Introduction Intellgent System
    </h5>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;เว็บไซต์นี้เป็นส่วนหนึ่งของรายวิชา 
                    <span style="background-color: #990000;">Intellgent System 040613701</span> 
                    ซึ่งมุ่งเน้นการศึกษาหลักการระบบอัจฉริยะพื้นฐานและการประยุกต์ใช้ 
                    Machine Learning และ Neural Network ในการแก้ปัญหาต่าง ๆ ในโลกความเป็นจริง
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    จุดประสงค์ของเว็บไซต์
    </h5>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - ให้ความเข้าใจเกี่ยวกับ ขั้นตอนการพัฒนาโมเดล AI ตั้งแต่การเตรียมข้อมูลไปจนถึงการนำไปใช้งาน<br>
                    - อธิบายทฤษฎีพื้นฐานของ Machine Learning และ Neural Network<br>
                    - สาธิตตัวอย่างการทำงานของโมเดล Machine Learning และ Neural Network<br> 
                    - แสดงให้เห็นถึง ความแตกต่าง ของอัลกอริทึม(Algorithm) แต่ละชนิด<br>
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    เนื้อหาภายในเว็บไซต์
    </h5>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - Introduction – แนะนำรายวิชาและวัตถุประสงค์ของเว็บไซต์<br>
                    - Algorithm & Model Development – อธิบายแนวทางการพัฒนาโมเดล Machine Learning และ Neural Network<br>
                    - Machine Learing Model – สาธิตการทำงานของโมเดล Machine Learning<br> 
                    - Neural Network Model – สาธิตการทำงานของโมเดล Neural Network<br>
                    <br>
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""
    <style>
        .about-container {
            text-align: center;
            font-family: 'Athiti', sans-serif;
        }
        .about-content {
            display: flex;
            justify-content: center;
            gap: 50px;
            font-size: 16px;
            text-align: left;
        }
    </style>
    <div class="about-container">
        <h5>About Us</h5>
        <div class="about-content">
            <div>
                <b>จัดทำโดย</b><br>
                นายพชร วรวัตร <br>
                รหัสนักศึกษา 6404062610324 <br>
                ห้อง DE-RA ชั้นปีที่ 4 <br>
            </div>
            <div>
                <b>อาจารย์ผู้สอน</b><br>
                ดร.ณัฐกิตติ์ จิตรเอื้อตระกูล (NJR) <br>
                ดร.ธรรศฏภณ สุระศักดิ์ (TSR) <br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


    with tab2:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    What is AI,ML,DL?🧐
    </h4>""", unsafe_allow_html=True)
        st.header("Artificial Intelligence :red[(AI)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;ปัญญาประดิษฐ์ หรือ AI คือ
                     ”ระบบ” ในการวิเคราะห์และประมวลผลที่มีความคล้ายคลึงกับความฉลาดของมนุษย์ 
                    และสามารถนำออกมาเป็นผลลัพธ์ต่างๆ เช่น การทำนายพฤติกรรมของลูกค้าใน 
                    E-Commerce หรือการวิเคราะห์อาการของผู้ป่วยจากข้อมูลต่างๆในโรงพยาบาล
    </p>""", unsafe_allow_html=True)
        
        st.header("Machine Learning :blue[(ML)]")

        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;Machine Learning คือ “การทำให้ระบบคอมพิวเตอร์สามารถเรียนรู้ได้ด้วยตนเองโดยใช้ข้อมูล” 
                    Machine Learning เป็น subset ของ AI จุดประสงค์คือเพื่อใช้ในการสร้างแอปพลิเคชั่นที่มีประสิทธิภาพมากกว่ามนุษย์ในการทำงานบางประเภท 
                    โดยการทำให้ฉลาดขึ้น สามารถพัฒนา และเรียนรู้ได้ด้วยตนเอง
    </p>""", unsafe_allow_html=True)
        
        st.header("Deep Learning :green[(DL)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;Deep Learning คือ “วิธีการเรียนรู้ลักษณะต่างๆ ของข้อมูล” โดยมีพื้นฐานการทำงานหรือการเรียนรู้จากระบบประสาทของสมองมุษย์ 
                    และ Deep Learning เป็น 
                    subset ของ Machine Learning อีกด้วย
    </p>""", unsafe_allow_html=True)
        
        st.image("img/ML-DL-AI.jpg",caption="How Difference of AI ML And DL")

    with tab3: 
        st.markdown("""<h4 style='font-family: Athiti; text-align: left;text-indent: 2.5em;'>
    🤖Why prepare data for artificial intelligence training?🤔
    </h4>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;โดยปกติตัว AI ก็คล้าย ๆ กับมนุษย์ทั่วไปนี่แหละ เปรียบเสมือนมนุษย์คนนึงจะแยกว่าอันไหนคือ 
                รถ หรือ คนได้ยังไง? ซึ่งคำตอบนั้นก็ง่าย ๆ ตรงตัวก็คือเราต้องเคยเห็นทั้ง รถและคนมาก่อน ว่ารถรูปร่างเป็นแบบไหนคนเป็นแบบไหนรูปร่างยังไง 
                แตกต่างกันอย่างไร เพราะว่าเรานั้นมีข้อมูลเยอะมากพอนั้นเอง (Data) แต่ถ้ามองในมุมกลับกัน ถ้าถามว่า รถที่เราไม่เคยเห็น 
                หรือมีรูปแบบที่เราไม่เคยเห็นมาก่อนก็อาจจะทำให้เรานั้นทายไม่ค่อยจะถูก เพราะว่าเรามี ข้อมูล(Data) ไม่เยอะมากพอหรือไม่เคยเห้นมากพอนั้นเอง
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;จากที่เกริ่นมาเราจะเห็นได้ว่า ข้อมูล(Data) ถ้ามีมากพอเราจะเรียนรู้สิ่งต่าง ๆ 
                ได้มากยิ่งขึ้น จากการเรียนรู้สิ่งต่าง ๆ ที่มากขึ้นตามไปนั้นเอง โดยทั้งหมดนี้ถ้าเราจะสร้าง AI ให้มันฉลาดหรือมีความแม่นยำที่สูงนั้นจำเป็นต้อง 
                มีข้อมูล(Data) เป็นจำนวนมากให้กับ ตัว AI เพื่อให้มันเรียนรู้จากข้อมูลที่เรานำไปสอนมัน 
                แล้วให้ตัว AI ค่อย ๆ ทำความเข้าใจจนสุดท้ายมันก็จะสร้าง Model ออกมานั้นเอง ยิ่งเรามี Data ให้มันเรียนรู้มากพอและหลากหลายจะทำให้ตัว AI ของเราก็จะยิ่งแม่นยำมากยิ่งขึ้นนั้นเอง
    </p>""", unsafe_allow_html=True)
        
        st.image("img/Blog_Selecting-the-Right-AI-Training-Data-is-Important.jpg",caption="How Intelligent of Artificial Intelligence")
        
    with tab4:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Source of Data Set🔎
    </h4>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;
    </p>""", unsafe_allow_html=True)
        
    with tab5:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Machine Learning📎
    </h4>""", unsafe_allow_html=True)
        
        st.header("Machine Learning :blue[(ML)]")
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;ที่มุ่งเน้นการพัฒนาอัลกอริธึม (Algorithm) และเทคนิคที่ช่วยให้คอมพิวเตอร์สามารถ
                        เรียนรู้จากข้อมูลได้โดยไม่จําเป็นต้องมีการเขียนโปรแกรมที่ชัดเจนสําหรับการทํางานแต่ละอย่าง การ
                        ทํางานของ Machine Learning จะขึ้นอยู่กับการฝึกสอนโมเดลด้วยข้อมูลจํานวนมาก ซึ่งโมเดลจะทําการ
                        วิเคราะห์และค้นหารูปแบบจากข้อมูลเหล่านั้น เพื่อให้สามารถทําการคาดการณ์หรือจําแนกประเภทข้อมูล
                        ใหม่ได้อย่างแม่นยํา
                        การเรียนรู้ของเครื่องแบ่งออกเป็นสามประเภทหลัก ๆ
    </p>""", unsafe_allow_html=True)
        
        st.header("- Supervised Learning :orange[(Label)]")

        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;การเรียนรู้แบบผู้สอน (Supervised Learning)
                    เป็นการเรียนรู้แบบโดยจะมีผู้สอน เรียกง่าย ๆคือ
                    โมเดลจะถูกฝึกสอนด้วยข้อมูลที่มีการติดป้ายกํากับ (Label) ซึ่งหมายถึงข้อมูลที่มีผลลัพธ์ที่ถูกต้องกํากับ
                    อยู่ เมื่อโมเดลได้รับข้อมูลนี้จะทําการเรียนรู้และสร้างฟังก์ชันเพื่อคาดการณ์ผลลัพธ์ที่ต้องการเมื่อได้รับ
                    ข้อมูลใหม่
    </p>""", unsafe_allow_html=True)
        
        st.header("- Unsupervised Learning :green[(Data Driven)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning) เป็นการเรียนรู้แบบรูปแบบไม่มีผู้สอน โมเดลจะ
                ทําการเรียนรู้จากข้อมูลที่ไม่มีการติดป้ายกํากับ ซึ่งจะเน้นในการค้นหารูปแบบหรือโครงสร้างที่ซ่อนอยู่ใน
                ข้อมูล การเรียนรู้แบบนี้มักถูกนํามาใช้ในงานที่ต้องการค้นหาความสัมพันธ์ระหว่างข้อมูลที่ไม่มีการจัด
                หมวดหมู่ เช่น การทําคลัสเตอร์ (Clustering) ที่ช่วยในการจัดกลุ่มข้อมูลที่มีลักษณะคล้ายกัน โดยไม่
                ต้องการข้อมูลที่มีการติดป้ายกํากับ
    </p>""", unsafe_allow_html=True)
        
        st.header("- Reinforcement Learning :gray[(Reward)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;การเรียนรู้แบบเสริมกําลัง (Reinforcement Learning) เป็นการเรียนรู้แบบเสริมเป็นวิธีการที่โมเดลจะ
                    ทําการทดลองและเรียนรู้จากผลตอบแทนหรือบทลงโทษที่ได้รับจากการกระทํา โดยในกระบวนการนี้
                    โมเดลจะเรียนรู้จากการลองผิดลองถูก เพื่อพัฒนากลยุทธ์ที่ดีที่สุดในการตัดสินใจในสถานการณ์ที่มีความ
                    ไม่แน่นอน ตัวอย่างการใช้ Reinforcement Learning คือการฝึกโมเดลให้เล่นเกม โดยโมเดลจะได้รับ
                    คะแนนเป็นผลตอบแทนเมื่อทําได้ดี และจะได้รับบทลงโทษเมื่อทําผิด
    </p>""", unsafe_allow_html=True)

        st.image("img/ML-Type.png",caption="How Difference of Type Learning")
    
    with tab6:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Neural Network🧠
    </h4>""", unsafe_allow_html=True)
        st.header("- Neural Network :red[(Weight&Bias)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
    &nbsp;&nbsp;&nbsp;อ้างอิงจากระบบประสาทในมนุษย์ ถูกออกแบบมาเพื่อให้
                สามารถเรียนรู้และประมวลผลข้อมูลได้อย่างมีประสิทธิภาพ โดยมีหน่วยประมวลผลที่เรียกว่า "นิวรอน"
                (Neurons) ที่ทําหน้าที่รับข้อมูล คํานวณ และส่งผลลัพธ์ไปยังนิวรอนในชั้นถัด ๆ ไป
                โครงสร้างของโครงข่ายประสาทเทียมแบ่งออกเป็นสามชั้นหลัก ได้แก่ ชั้นนําเข้าข้อมูล (Input Layer)
                ที่ใช้สําหรับรับข้อมูลที่จะวิเคราะห์ ชั้นซ่อน (Hidden Layers) ซึ่งอยู่ระหว่างชั้นนําเข้าและชั้นส่งออก ซึ่ง
                อาจมีหลายชั้น และชั้นส่งออก (Output Layer) ที่ให้ผลลัพธ์สุดท้ายจากการประมวลผลข้อมูล
                เมื่อข้อมูลถูกส่งเข้ามายังโครงข่าย นิวรอนแต่ละตัวจะใช้ฟังก์ชันการกระตุ้น (Activation Function) ใน
                การคํานวณเพื่อกําหนดว่านิวรอนจะส่งข้อมูลไปยังชั้นถัดไปหรือไม่ การคํานวณนี้จะใช้ "น้ําหนัก"
                (Weights) และ "อคติ" (Bias) เป็นปัจจัยสําคัญ
                น้ําหนัก (Weights) เป็นค่าที่แสดงถึงความสําคัญของข้อมูลที่ส่งเข้าสู่นิวรอนแต่ละตัว โดยค่าของ
                น้ําหนักจะถูกปรับในระหว่างกระบวนการฝึกอบรม (Training) เพื่อเพิ่มความแม่นยําในการจําแนก
                ประเภทหรือลงทํานายผลลัพธ์ ค่าน้ําหนักที่สูงบ่งบอกว่าข้อมูลนั้นมีความสําคัญในกระบวนการคํานวณ
                มากขึ้น
                อคติ (Bias) ช่วยเพิ่มความยืดหยุ่นให้กับผลลัพธ์ของนิวรอน โดยทําหน้าที่เป็นค่าที่ถูกเพิ่มเข้ามาในการ
                คํานวณ ทําให้โครงข่ายสามารถปรับตัวเข้ากับข้อมูลได้ดีขึ้น และช่วยสร้างผลลัพธ์ที่มีประสิทธิภาพ แม้ใน
                กรณีที่ข้อมูลมีลักษณะเฉพาะหรือไม่เป็นเชิงเส้น
                <span style="background-color: #990000;">"โดยการฝึกอบรมโครงข่ายประสาทเทียมมักใช้เทคนิคที่เรียกว่า การย้อนกลับ (Backpropagation) เพื่อ
                ปรับปรุงน้ําหนัก (Weights) และอคติ(Bias) โดยการคํานวณค่าความผิดพลาด (Error) ระหว่างผลลัพธ์ที่
                ทํานายและค่าจริง แล้วทําการปรับน้ําหนัก (Weights) และอคติ(Bias) เพื่อลดค่าความผิดพลาด " (Neurons)</span>
    </p>""", unsafe_allow_html=True)
        file_ = open("img/visuNN.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,)

def show_model_development():
    st.title("Model Development")
    st.write("""
    ## ขั้นตอนการพัฒนาโมเดล
    ### Machine Learning
    - ใช้อัลกอริทึม เช่น Decision Trees, SVM, Random Forest
    - Feature Engineering และ Hyperparameter Tuning
    
    ### Neural Network
    - ใช้โครงข่ายประสาทเทียม เช่น CNN, RNN, Transformer
    - การปรับแต่งโครงสร้างโมเดลและ Learning Rate
    """)

if __name__ == "__main__":
    main()