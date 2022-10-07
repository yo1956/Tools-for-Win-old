from genericpath import exists
import os

# 元々はあるファイルの存在を確認してReleaseモード、Debugモードを判断していたアプリケーションの、モード制御用スクリプト
# 手で対象ファイルをリネームするのが面倒だったため作った

# 以下のパスやファイル名を書き換えて使用
SearchFolder = r"C:~"
DebugFileName1 = r"~.ini"
DebugFileName2 = r"~.xml"
ReleaseFileName1 = r"~.ini__"
ReleaseFileName2 = r"~.xml__"

DebugModeFullPath1 = SearchFolder + DebugFileName1
DebugModeFullPath2 = SearchFolder + DebugFileName2
ReleaseModeFullPath1 = SearchFolder +ReleaseFileName1
ReleaseModeFullPath2 = SearchFolder +ReleaseFileName2


#デバッグモードの場合
if os.path.exists(DebugModeFullPath1) & os.path.exists(DebugModeFullPath2):
    print('CurrentMode: Debug')
    #ユーザ入力確認
    user_input = input("ModeChange? (y/n) >>")

    #リリースモードに変更
    if user_input == 'y':
        os.rename(DebugModeFullPath1, ReleaseModeFullPath1)
        os.rename(DebugModeFullPath2, ReleaseModeFullPath2)

        print(DebugFileName1 + '→' + ReleaseFileName1)
        print(DebugFileName2 + '→' + ReleaseFileName2)
        print('Debug→Release Mode Change Complete')
    
    else:
        print('exit')

#リリースモードの場合
elif os.path.exists(ReleaseModeFullPath1) & os.path.exists(ReleaseModeFullPath2):
    print('CurrentMode: Release')
    #ユーザ入力確認
    user_input = input("ModeChange? (y/n) >>")

    #デバッグモードに変更
    if user_input == 'y':
        os.rename(ReleaseModeFullPath1, DebugModeFullPath1)
        os.rename(ReleaseModeFullPath2, DebugModeFullPath2)

        print(ReleaseFileName1 + '→' + DebugFileName1)
        print(ReleaseFileName2 + '→' + DebugFileName2)
        print('Release→Debug Mode Change Complete')
    else:
        print('exit')
    
else:
    print('error')