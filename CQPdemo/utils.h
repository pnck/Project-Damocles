#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

#include <Shlwapi.h>
#pragma comment(lib, "Shlwapi.lib")

std::vector<std::string> str_list();
std::vector<std::string> str_list(const std::string& item1);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6, const std::string& item7);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6, const std::string& item7, const std::string& item8);
std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6, const std::string& item7, const std::string& item8, const std::string& item9);

// 字符串工具
std::string str_tolower(const std::string& str);
std::string str_toupper(const std::string& str);
std::string str_strip(const std::string& str);
std::vector<std::string> str_split(const std::string& str, char sp, unsigned max = 0);
std::vector<std::string> str_split(const std::string& str, const std::string& sp, unsigned max = 0);
int str_compare_ignore_case(const std::string& str1, const std::string& str2);
bool str_starts_with(const std::string& str, const std::string& sub);
bool str_ends_with(const std::string& str, const std::string& sub);
bool str_starts_with_ignore_case(const std::string& str, const std::string& sub);
bool str_ends_with_ignore_case(const std::string& str, const std::string& sub);
std::string str_replace(const std::string& str, char from, char to);
std::string str_replace(const std::string& str, const std::string& from, const std::string& to);
std::string str_join(const std::string& sp, const std::vector<std::string>& items);
std::string str_join(const std::vector<std::string>& items);
std::string str_gb2312_to_utf8(std::string str_gb2312);
std::string str_utf8_to_gb2312(std::string str_utf8);

//　路径工具
bool os_chdir(const std::string& pathname);
std::string os_getcwd();
std::string os_getmodulefilename(HMODULE hModule);
void os_makedirs(const std::string& pathname);
std::vector<std::string> os_listdir(const std::string& pathname, const std::string& filter = "*");
bool os_remove(const std::string& pathname);
bool os_rmdir(const std::string& pathname);
bool os_removedirs(const std::string& pathname);
bool os_move(const std::string& oldname, const std::string& newname);
bool os_copy(const std::string& oldname, const std::string& newname);
bool os_rename(const std::string& oldname, const std::string& newname);
void os_delpuv(const std::string& name);
void os_putenv(const std::string& name, const std::string& value);
std::string os_getenv(const std::string& name);
std::string os_tempdir();
std::string os_tempfilename(const std::string& tempdir, const std::string& prefix);
std::string path_abspath(const std::string& pathname);
std::string path_relname(const std::string& from_pathname, const std::string& to_pathname);
std::string path_basename(const std::string& pathname);
std::string path_dirname(const std::string& pathname);
bool path_exists(const std::string& pathname);
time_t path_getmtime(const std::string& pathname);
size_t path_getsize(const std::string& pathname);
bool path_isrel(const std::string& pathname);
bool path_isabs(const std::string& pathname);
bool path_isdir(const std::string& pathname);
bool path_isfile(const std::string& pathname);
std::string path_join(const std::vector<std::string>& items);
std::vector<std::string> path_split(const std::string& pathname);
std::vector<std::string> path_splitext(const std::string& pathname);

// 文件工具
std::vector<std::string> file_readlines(const std::string& filename);
