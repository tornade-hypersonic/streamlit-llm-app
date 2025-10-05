from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st

load_dotenv()


st.title("課題アプリ: LLMアプリ")

st.write("##### 動作モード1: Pythonの専門家")
st.write("Pythonの専門家として回答します。")
st.write("##### 動作モード2: Javaの専門家")
st.write("Javaの専門家として回答します。")

selected_mode = st.radio(
    "動作モードを選択してください", ("Pythonの専門家", "Javaの専門家")
)

input_message = st.text_area("質問を入力してください", key="question")

if st.button("実行"):
    if selected_mode == "Pythonの専門家":
        system_content = "あなたはPythonの専門家です。"
    else:
        system_content = "あなたはJavaの専門家です。"

    try:
        # print(f"System Content: {system_content}")
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, verbose=True)
        messages = [
            SystemMessage(content=system_content),
            HumanMessage(content=input_message),
        ]
        response = llm(messages)
        st.write("##### 回答")
        st.write(response.content)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
        st.stop()
