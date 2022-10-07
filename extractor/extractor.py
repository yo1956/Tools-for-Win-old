
# 指定ファイルから指定文字列を含むレコードを抽出
def extract_record(arg_file_path: str, arg_extract_target):
    with open(arg_file_path, "r", encoding="shift_jis") as file:
        lines = file.readlines() #ファイルの各行を要素とするリストを取得
    
   # lines_strip = [line.strip() for line in lines] #改行文字を削除
   # lines_target = [line for line in lines_strip if arg_extract_target in line] #指定した文字列を含む行を抽出

    lines_target = [line for line in lines if arg_extract_target in line] #指定した文字列を含む行を抽出
    
    file_out = open('result_extract.txt', 'w', encoding='UTF-8')
    file_out.writelines(lines_target)
    file_out.close()


def main():

    while True:

        # 対象ファイルのパス取得
        user_input = input("ここに処理したいファイルをドラッグ＆ドロップ-> :")

        extract_target = input("何の文字列を含むレコードを抽出するか(スレッドIDなどを入力):") 

        # 「"」を取り除く
        target_file_path = user_input.replace("\"","")

        # 抽出
        extract_record(target_file_path, extract_target)

        print("All process complete\n")


# 実行
if __name__ == '__main__':
    main()
