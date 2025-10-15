import streamlit as st
import re

# 文章修正関数
def correct_text(input_text):
    lines = input_text.split('\n')
    lines = [line for line in lines if line.strip() != '']
    cleaned_lines = []
    for line in lines:
        line = line.replace('　', ' ')
        line = re.sub(r'\\s+', ' ', line)
        line = line.strip()
        line = re.sub(r'([!?.…])\\s+', r'\\1', line)
        line = re.sub(r'\\s+([!?.…])', r'\\1', line)
        line = re.sub(r'「\\)。」', r'」', line)
        line = line.replace(' ', '')
        cleaned_lines.append(line)
    indented_lines = []
    for line in cleaned_lines:
        if line.startswith('「'):
            indented_lines.append(line)
        else:
            indented_lines.append('　' + line)
    return '\n'.join(indented_lines)

def correct_text(input_text):
    lines = input_text.split('\\n')
    lines = [line for line in lines if line.strip() != '']
    cleaned_lines = []
    for line in lines:
        line = line.replace('　', ' ')
        line = re.sub(r'\\s+', ' ', line)
        line = line.strip()
        line = re.sub(r'([!?.…])\\s+', r'\\1', line)
        line = re.sub(r'\\s+([!?.…])', r'\\1', line)
        line = re.sub(r'「\\)。」', r'」', line)
        line = line.replace(' ', '')
        cleaned_lines.append(line)
    indented_lines = []
    for line in cleaned_lines:
        if line.startswith('「'):
            indented_lines.append(line)
        else:
            indented_lines.append('　' + line)
    return '\\n'.join(indented_lines)

st.set_page_config(page_title="⭐", page_icon="🚀")
st.title("🚀")

input_method = st.radio("入力方法を選択してください:", ("ファイルアップロード", "テキスト入力"))
input_text = ""
if input_method == "テキスト入力":
    input_text = st.text_area("ここにテキストを入力してください:", height=200, placeholder="生存と繁殖に代わり、真実と好奇心の追求が新本能になる。")
else:
    uploaded_file = st.file_uploader("テキストファイル（例: 原稿.txt）をアップロード", type=["txt"])
    if uploaded_file is not None:
        input_text = uploaded_file.read().decode("utf-8")

if st.button("修正実行", key="process_button"):
    if input_text:
        with st.spinner("処理中..."):
            corrected_text = correct_text(input_text)
        st.subheader("修正結果")
        st.text_area("修正されたテキスト:", corrected_text, height=200)
        st.download_button(
            label="修正済み原稿をダウンロード",
            data=corrected_text.encode('utf-8'),
            file_name="修正済み原稿.txt",
            mime="text/plain"
        )
    else:

        st.error("テキストを入力またはファイルをアップロードしてください。")

