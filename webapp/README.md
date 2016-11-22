# 在学习这个简单的项目过程中，遇到的坑

## Error code 403.

- 描述：运行服务端后，进入`http://localhost:8080/cgi-bin/generate_list.py`时，提示**403**
> Error code 403
> Message: CGI script is not executable ('/cgi-bin/generate_list.py').

- 原因：使用 PyCharm 创建的 py 文件没有可执行权限！

- 解决方法：chrom +x generate_list.py
    (generate_timing_data.py 也是同理)

感谢 stackoverflow！
`http://stackoverflow.com/questions/13386795/cgi-script-is-not-executable`