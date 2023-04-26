# setup-py-example
[https://setuptools.pypa.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies](https://setuptools.pypa.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies)

- Python packageを作成する。
- setup.cfg設定ファイルを記述することで本来setup.pyのsetup()に引数を指定する必要があったが不要になる
    - 可読性を考えてsetup.cfgに記述するほうが好ましい
- setup.cfgの書き方
[https://setuptools.pypa.io/en/latest/userguide/declarative_config.html](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)
- setup.cfgには最低限 options.packages, package_dirを書く
- setup.cfgが書き終わったら、 `python -m build` する
(事前にbuildをpip install しておく)
- distフォルダに出来上がったwhlファイルを手元にインストールして確認する。
    - venvなどを用意して、pip installを実行しwhlファイルをインストールしてパッケージが使用できるか確認する。
        ```
        pip install dist/hoge-0.0.0-py3-none-any.whl hoge
        ```
