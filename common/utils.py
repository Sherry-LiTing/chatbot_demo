from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores.chroma import Chroma


def get_embedding(model_name):
    # embedding設定
    embedding = HuggingFaceEmbeddings(model_name=model_name)
    return embedding


def create_chroma(dir, documents, embedding):
    # データベースをロード（ローカルに保存）
    db = Chroma.from_documents(
        documents=documents,  # テキスト分割済データ
        persist_directory=dir,  # データベースの保存先
        embedding=embedding,  # Embeddings関数
    )

    # ローカルに書き込み
    db.persist()

def load_chroma(dir_path, embedding) -> Chroma:
    return Chroma(
        #  データベースの保存先
        persist_directory=dir_path,  
        # Embeddings関数
        embedding_function=embedding,  
    )
    
def load_languages(file):
    file_content = ""
    # ファイル内容の読み取り
    with open(file, mode='r', encoding="utf-8") as f:
        file_content = f.read()
        
    # 内容を分割
    languages = file_content.strip().split("\n\n")   
    
    docs = []
    # ドキュメントの解析と保存  
    for langusge in languages:
        doc = Document(page_content=f"{langusge}")
        docs.append(doc)
    
    return docs

EMBEDDING = get_embedding("BAAI/bge-m3")
# データベースの保存先
COMPANYINFO_DB = load_chroma('index/bge-m3/company_info', EMBEDDING)

if __name__ == "__main__":
    
    model_name = "BAAI/bge-m3"
    embedding = get_embedding(model_name)
    
    file = "data/company_info.txt"
    dir_path = "index/bge-m3/company_info"
    
    docs = load_languages(file)
    
    create_chroma(dir_path, docs, embedding)
    
    
    
    



        
        
    
    
      
