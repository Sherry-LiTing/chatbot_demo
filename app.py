
import logging

# ログ設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler() 
    ]
)

if __name__ == "__main__":
    from chats import search_company_info as sci
    from chainlit.cli import run_chainlit

    # ファイルパスを取得
    file_path = sci.__file__
    run_chainlit(file_path)
    