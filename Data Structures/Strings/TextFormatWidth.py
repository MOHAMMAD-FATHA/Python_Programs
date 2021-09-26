"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:15
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:15
* @Title: : Python program to get string in list of strings
"""
import textwrap
sample_text = '''
    * @Author: Mohammad Fatha
`   * @Date: 2021-09-27 02:15
    * @Last Modified by: Mohammad Fatha
    * @Last Modified time: 2021-09-27 02:15
    * @Title: : Python program to get string in list of strings
  '''
print()
print(textwrap.fill(sample_text, width=100))
print()