import os
import glob
import datetime
import shutil

# -----------------   設定   --------------------------------------

# 移動したいファイル（とりあえず正規表現）
move_path_list = [ r"C:",   # パスを記載
                 ] 

# コピーしたいファイル（そのままファイルパス）
copy_path_list = [ r"C:",   # パスを記載
                 ]

# 移動・コピー先 ディレクトリ
target_path = r"C:\Users\¥" # パスを記載

# ------------------------------------------------------------------

# 移動したいファイルリスト作成
move_file_list = []
move_file_path_list = []
for t_move_path in move_path_list:
    t_file_path_list = glob.glob(t_move_path)
    move_file_list += [os.path.basename(x) for x in t_file_path_list]
    move_file_path_list += t_file_path_list

# コピーしたいファイルリスト作成
copy_file_list = []
for t_copy_path in copy_path_list:
    copy_file_list.append(os.path.basename(t_copy_path))

# 移動先フォルダパス作成
now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_folder_path = os.path.join(target_path, f"{now_time}")

# 移動するか確認
#print(f"Move File List")
print(f"移動するファイル一覧")
for idx,move_file in enumerate(move_file_list):
    print(f"    [{idx}] : {move_file}")
print("---------------")
#print(f"Copy File List")
print(f"コピーするファイル一覧")
for idx,copy_file in enumerate(copy_file_list):
    print(f"    [{idx}] : {copy_file}")
print("---------------")
# print(f"Out directory : {output_folder_path}")
print(f"移動・コピー先フォルダ")
print(f"    [0] : {output_folder_path}")
print("---------------")

# ユーザ入力確認
user_input = input("ファイルの移動・コピーしますか？ (y/n) >>")

# ファイル移動する
if user_input == 'y':

    # 移動先フォルダ作成
    if os.path.exists(output_folder_path) is False:
        print(f"CREATE \"{output_folder_path}\"")
        os.makedirs(output_folder_path)

    # ファイル移動
    for t_move_file_path in move_file_path_list:
        t_file_name = os.path.basename(t_move_file_path)
        t_target_file_path = os.path.join(output_folder_path, t_file_name)
        print(f"MOVE \"{t_file_name}\" FROM \"{t_move_file_path}\" TO \"{t_target_file_path}\" ")
        os.rename(t_move_file_path, t_target_file_path)

    # ファイルコピー
    for t_copy_file_path in copy_path_list:
        t_file_name = os.path.basename(t_copy_file_path)
        t_target_file_path = os.path.join(output_folder_path, t_file_name)
        print(f"COPY \"{t_file_name}\" FROM \"{t_copy_file_path}\" TO \"{t_target_file_path}\" ")
        shutil.copy(t_copy_file_path, t_target_file_path)
    print("COMPLETE")
else:
    print ("CANCELED")
