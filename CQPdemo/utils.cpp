#include "stdafx.h"
#include "utils.h"

//////////////////////////////////////////////////////////////////////////

std::vector<std::string> str_list()
{
	std::vector<std::string> items;
	return items;
}

std::vector<std::string> str_list(const std::string& item1)
{
	std::vector<std::string> items;
	items.push_back(item1);
	return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2)
{
    std::vector<std::string> items;
    items.push_back(item1);
    items.push_back(item2);
    return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3)
{
    std::vector<std::string> items;
    items.push_back(item1);
    items.push_back(item2);
    items.push_back(item3);
    return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4)
{
    std::vector<std::string> items;
    items.push_back(item1);
    items.push_back(item2);
    items.push_back(item3);
    items.push_back(item4);
    return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5)
{
	std::vector<std::string> items;
	items.push_back(item1);
	items.push_back(item2);
	items.push_back(item3);
	items.push_back(item4);
	items.push_back(item5);
	return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6)
{
	std::vector<std::string> items;
	items.push_back(item1);
	items.push_back(item2);
	items.push_back(item3);
	items.push_back(item4);
	items.push_back(item5);
	items.push_back(item6);
	return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6, const std::string& item7)
{
	std::vector<std::string> items;
	items.push_back(item1);
	items.push_back(item2);
	items.push_back(item3);
	items.push_back(item4);
	items.push_back(item5);
	items.push_back(item6);
	items.push_back(item7);
	return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6, const std::string& item7, const std::string& item8)
{
	std::vector<std::string> items;
	items.push_back(item1);
	items.push_back(item2);
	items.push_back(item3);
	items.push_back(item4);
	items.push_back(item5);
	items.push_back(item6);
	items.push_back(item7);
	items.push_back(item8);
	return items;
}

std::vector<std::string> str_list(const std::string& item1, const std::string& item2, const std::string& item3, const std::string& item4, const std::string& item5, const std::string& item6, const std::string& item7, const std::string& item8, const std::string& item9)
{
	std::vector<std::string> items;
	items.push_back(item1);
	items.push_back(item2);
	items.push_back(item3);
	items.push_back(item4);
	items.push_back(item5);
	items.push_back(item6);
	items.push_back(item7);
	items.push_back(item8);
	items.push_back(item9);
	return items;
}


//////////////////////////////////////////////////////////////////////////

std::string str_tolower(const std::string& str)
{
    std::string ret = str;
    for (size_t i = 0; i < ret.length(); i++)
    {
        if (ret[i] >= 'A' && ret[i] <= 'Z')
        {
            ret[i] = tolower(ret[i]);
        }
    }
    return ret;
}

std::string str_toupper(const std::string& str)
{
    std::string ret = str;
    for (size_t i = 0; i < ret.length(); i++)
    {
        if (ret[i] >= 'a' && ret[i] <= 'z')
        {
            ret[i] = toupper(ret[i]);
        }
    }
    return ret;
}

std::string str_strip(const std::string& str)
{
    if (!str.empty())
    {
        size_t lindex = 0;
        for (; lindex < str.length(); lindex++)
        {
            if (!isspace(str[lindex]))
            {
                break;
            }
        }
        size_t rindex = str.length() - 1;
        for (; rindex > lindex; rindex--)
        {
            if (!isspace(str[rindex]))
            {
                break;
            }
        }
        return str.substr(lindex, rindex - lindex + 1);
    }
    return str;
}

std::vector<std::string> str_split(const std::string& str, char sp, unsigned max /*= 0*/)
{
    std::vector<std::string> arr;
    if (max == 1 || str.empty())
    {
        arr.push_back(str);
    }
    else
    {
        int offset = 0;
        while (true)
        {
            int spindex = str.find_first_of(sp, offset);
            if (spindex >= 0)
            {
                arr.push_back(str.substr(offset, spindex - offset));
                offset = spindex + 1;
                if ((arr.size() + 1) == max)
                {
                    arr.push_back(str.substr(offset));
                    break;
                }
            }
            else
            {
                arr.push_back(str.substr(offset));
                break;
            }
        }
    }
    return arr;
}


std::vector<std::string> str_split(const std::string& str, const std::string& sp, unsigned max /*= 0*/)
{
    std::vector<std::string> arr;
    if (max == 1 || sp.empty())
    {
        arr.push_back(str);
    }
    else
    {
        int offset = 0;
        while (true)
        {
            int spindex = str.find_first_of(sp, offset);
            if (spindex >= 0)
            {
                arr.push_back(str.substr(offset, spindex - offset));
                offset = spindex + sp.length();
                if ((arr.size() + 1) == max)
                {
                    arr.push_back(str.substr(offset));
                    break;
                }
            }
            else
            {
                arr.push_back(str.substr(offset));
                break;
            }
        }
    }
    return arr;
}

int str_compare_ignore_case(const std::string& str1, const std::string& str2)
{
    return str_tolower(str1).compare(str_tolower(str2));
}

bool str_starts_with(const std::string& str, const std::string& sub)
{
    return str.substr(0, sub.length()).compare(sub) == 0;
}

bool str_ends_with(const std::string& str, const std::string& sub)
{
    return str.substr(str.length() - sub.length()).compare(sub) == 0;
}

bool str_starts_with_ignore_case(const std::string& str, const std::string& sub)
{
    return str_compare_ignore_case(str.substr(0, sub.length()), sub) == 0;
}

bool str_ends_with_ignore_case(const std::string& str, const std::string& sub)
{
    return str_compare_ignore_case(str.substr(str.length() - sub.length()), sub) == 0;
}

std::string str_replace(const std::string& str, char from, char to)
{
    std::string ret = str;
    for (size_t i = 0; i < ret.length(); i++)
    {
        if (ret[i] == from)
        {
            ret[i] = to;
        }
    }
    return ret;
}

std::string str_replace(const std::string& str, const std::string& from, const std::string& to)
{
    std::stringstream ss;
    size_t offset = 0;
    while (true)
    {
        size_t findex = str.find_first_of(from, offset);
        if (findex >= 0)
        {
            ss << str.substr(offset, findex) << to;
            offset += from.length();
        }
        else
        {
            ss << str.substr(offset);
            break;
        }
    }
    return ss.str();
}

std::string str_join(const std::string& sp, const std::vector<std::string>& items)
{
    std::stringstream ss;
    if (!items.empty())
    {
        size_t index = 0;
        ss << items[index];
        while ((++index) < items.size())
        {
            ss << sp << items[index];
        }
    }
    return ss.str();
}

std::string str_join(const std::vector<std::string>& items)
{
    std::stringstream ss;
    for (std::vector<std::string>::const_iterator it = items.begin(); it != items.end(); it++)
    {
        ss << (*it);
    }
    return ss.str();
}

std::string str_gb2312_to_utf8(std::string str_gb2312)
{
	size_t n_unicode = ::MultiByteToWideChar(CP_ACP, 0, str_gb2312.c_str(), -1, NULL, 0);
	wchar_t* buffer_unicode = new wchar_t[n_unicode + 1];
	::MultiByteToWideChar(CP_ACP, 0, str_gb2312.c_str(), -1, buffer_unicode, n_unicode);

	size_t n_utf8 = ::WideCharToMultiByte(CP_UTF8, 0, buffer_unicode, -1, NULL, 0, NULL, NULL);
	char* buffer_utf8 = new char[n_utf8 + 1];
	::WideCharToMultiByte(CP_UTF8, 0, buffer_unicode, -1, buffer_utf8, n_utf8, NULL, NULL);

	std::string str_utf8 = std::string(buffer_utf8);

	delete[] buffer_utf8;
	delete[] buffer_unicode;

	return str_utf8;
}

std::string str_utf8_to_gb2312(std::string str_utf8)
{
	size_t n_unicode = ::MultiByteToWideChar(CP_UTF8, 0, str_utf8.c_str(), -1, NULL, 0);
	wchar_t* buffer_unicode = new wchar_t[n_unicode + 1];
	::MultiByteToWideChar(CP_UTF8, 0, str_utf8.c_str(), -1, buffer_unicode, n_unicode);

	size_t n_gb2312 = ::WideCharToMultiByte(CP_ACP, 0, buffer_unicode, -1, NULL, 0, NULL, NULL);
	char* buffer_gb2312 = new char[n_gb2312 + 1];
	::WideCharToMultiByte(CP_ACP, 0, buffer_unicode, -1, buffer_gb2312, n_gb2312, NULL, NULL);

	std::string str_gb2312 = std::string(buffer_gb2312);

	delete[] buffer_gb2312;
	delete[] buffer_unicode;

	return str_gb2312;
}

//////////////////////////////////////////////////////////////////////////
bool os_chdir(const std::string& pathname)
{
    return (FALSE != ::SetCurrentDirectoryA(pathname.c_str()));
}

std::string os_getcwd()
{
    const size_t bufsize = MAX_PATH + 1;
    char buffer[bufsize];
    memset(buffer, 0, sizeof(char) * bufsize);
    DWORD n = ::GetCurrentDirectoryA(bufsize, buffer);
    buffer[n] = '\0';
    return std::string(buffer);
}

std::string os_getmodulefilename(HMODULE hModule /* = NULL */)
{
    const size_t bufsize = MAX_PATH + 1;
    char buffer[bufsize];
    memset(buffer, 0, sizeof(char) * bufsize);
    DWORD n = ::GetModuleFileNameA(hModule, buffer, bufsize);
    buffer[n] = '\0';
    return std::string(buffer);
}

void os_makedirs(const std::string& pathname)
{
    const std::vector<std::string>& items = path_split(pathname);

    if (!items.empty())
    {
        size_t index = 0;
        std::string dirname = items[index++];
        while (true)
        {
            ::CreateDirectoryA(dirname.c_str(), NULL);
            if (index < items.size())
            {
                dirname = path_join(str_list(dirname, items[index++]));
            }
            else
            {
                break;
            }
        }
    }
}

std::vector<std::string> os_listdir(const std::string& pathname, const std::string& filter /*= "*"*/)
{
    std::vector<std::string> items;

    WIN32_FIND_DATAA w32fd;

    std::string pathname_t = path_join(str_list(pathname, filter));
    HANDLE hFindFile = ::FindFirstFileA(pathname_t.c_str(), &w32fd);
    if (INVALID_HANDLE_VALUE != hFindFile)
    {
        do
        {
            items.push_back(w32fd.cFileName);
        } while (FALSE != ::FindNextFileA(hFindFile, &w32fd));
        ::FindClose(hFindFile);
    }
    return items;
}

bool os_remove(const std::string& pathname)
{
    return (FALSE != ::DeleteFileA(pathname.c_str()));
}

bool os_rmdir(const std::string& pathname)
{
    return (FALSE != ::RemoveDirectoryA(pathname.c_str()));
}

bool os_removedirs(const std::string& pathname)
{
    std::vector<std::string>& items = os_listdir(pathname);
    for (std::vector<std::string>::iterator it = items.begin(); it != items.end(); it++)
    {
        if (path_isdir(*it))
        {
            os_removedirs(*it);
        }
        else
        {
            os_remove(*it);
        }
    }
    return os_rmdir(pathname);
}


bool os_move(const std::string& oldname, const std::string& newname)
{
    return (FALSE != ::MoveFileA(oldname.c_str(), newname.c_str()));
}

bool os_copy(const std::string& oldname, const std::string& newname)
{
    return (FALSE != ::CopyFileA(oldname.c_str(), newname.c_str(), FALSE));
}

bool os_rename(const std::string& oldname, const std::string& newname)
{
    return os_move(oldname, newname);
}

void os_delpuv(const std::string& name)
{
    ::SetEnvironmentVariableA(name.c_str(), NULL);
    _putenv(str_join(str_list(name, "=")).c_str());
}

void os_putenv(const std::string& name, const std::string& value)
{
    ::SetEnvironmentVariableA(name.c_str(), value.c_str());
    _putenv(str_join(str_list(name, "=", value)).c_str());
}

std::string os_getenv(const std::string& name)
{
	std::string ret;

	char* buffer;
	size_t buffer_size;
	errno_t err = _dupenv_s(&buffer, &buffer_size, name.c_str());
	if (!err)
	{
		if (buffer)
		{
			ret = std::string(buffer);
			free(buffer);
		}
	}

	return ret;
}

std::string os_tempdir()
{
    const size_t bufsize = MAX_PATH + 1;
    char buffer[bufsize];
    memset(buffer, 0, sizeof(char) * bufsize);
    DWORD n = ::GetTempPathA(bufsize, buffer);
    buffer[n] = '\0';
    return std::string(buffer);
}

std::string os_tempfilename(const std::string& tempdir, const std::string& prefix)
{
    const size_t bufsize = MAX_PATH + 1;
    char buffer[bufsize];
    memset(buffer, 0, sizeof(char) * bufsize);
    ::GetTempFileNameA(tempdir.c_str(), prefix.c_str(), 0, buffer);
    return std::string(buffer);
}

std::string path_abspath(const std::string& pathname)
{
    std::vector<std::string> items_t = path_split((path_isrel(pathname)) ? (path_join(str_list(os_getcwd(), pathname))) : (pathname));
    std::vector<std::string> items;

    for (size_t index = 0; index < items_t.size(); index++)
    {
        const std::string& item = items_t[index];
        if (item.compare(".") == 0)
        {
            continue;
        }
        else if (item.compare("..") == 0)
        {
            items.pop_back();
        }
        else
        {
            items.push_back(item);
        }
    }

    return path_join(items);
}

std::string path_relname(const std::string& from_pathname, const std::string& to_pathname)
{
    const std::vector<std::string>& items_from = path_split(path_abspath(from_pathname));
    const std::vector<std::string>& items_to = path_split(path_abspath(to_pathname));

    size_t minlen = min(items_from.size(), items_to.size());
    size_t index = 0;
    for (; index < minlen; index++)
    {
        if (str_compare_ignore_case(items_from[index], items_to[index]) != 0)
        {
            break;
        }
    }

    if (index > 0)
    {
        std::vector<std::string> items;

        int level = items_from.size() - index;
        if (level > 1)
        {
            while (--level)
            {
                items.push_back("..");
            }
        }
        else
        {
            items.push_back(".");
        }

        for (size_t i = index; i < items_to.size(); i++)
        {
            items.push_back(items_to[i]);
        }

        return path_join(items);
    }

    return to_pathname;
}

std::string path_basename(const std::string& pathname)
{
    std::string pathname_t = str_replace(pathname, '/', '\\');
    size_t last_sp_index = pathname_t.find_last_of('\\');

    std::string basename = "";

    if (last_sp_index >= (pathname_t.length() - 1))
    {
        return "";
    }
    else if (last_sp_index >= 0)
    {
        return pathname_t.substr(last_sp_index + 1);
    }
    else
    {
        basename = pathname_t;
    }

    return basename;
}

std::string path_dirname(const std::string& pathname)
{
    std::string pathname_t = str_replace(pathname, '/', '\\');
    size_t last_sp_index = pathname_t.find_last_of('\\');
    if (last_sp_index >= 0)
    {
        return pathname_t.substr(0, last_sp_index);
    }
    return "";
}

bool path_exists(const std::string& pathname)
{
    DWORD attr = ::GetFileAttributesA(pathname.c_str());
    bool ret = (attr != INVALID_FILE_ATTRIBUTES);
    return ret;
}

time_t path_getmtime(const std::string& pathname)
{
    HANDLE hFile = ::CreateFileA(pathname.c_str(), GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, NULL, NULL);
    if (INVALID_HANDLE_VALUE != hFile)
    {
        FILETIME ctime, atime, mtime;
        if (FALSE != ::GetFileTime(hFile, &ctime, &atime, &mtime))
        {
            ULARGE_INTEGER ui;
            ui.LowPart = mtime.dwLowDateTime;
            ui.HighPart = mtime.dwHighDateTime;

            time_t t = ((LONGLONG)(ui.QuadPart - 116444736000000000) / 10000000);
            ::CloseHandle(hFile);
            return t;
        }
    }
    return 0;
}

size_t path_getsize(const std::string& pathname)
{
    HANDLE hFile = ::CreateFileA(pathname.c_str(), GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, NULL, NULL);
    if (INVALID_HANDLE_VALUE != hFile)
    {
        size_t s = ::GetFileSize(hFile, NULL);
        ::CloseHandle(hFile);
        return s;
    }
    return 0;
}

bool path_isrel(const std::string& pathname)
{
    return (FALSE != ::PathIsRelativeA(pathname.c_str()));
}

bool path_isabs(const std::string& pathname)
{
    return !path_isrel(pathname);
}

bool path_isdir(const std::string& pathname)
{
    DWORD attr = ::GetFileAttributesA(pathname.c_str());
    bool ret = ((attr != INVALID_FILE_ATTRIBUTES)
        && ((attr & FILE_ATTRIBUTE_ARCHIVE) != 0)
        && ((attr & FILE_ATTRIBUTE_DIRECTORY) != 0));

    return ret;
}

bool path_isfile(const std::string& pathname)
{
    DWORD attr = ::GetFileAttributesA(pathname.c_str());
    bool ret = ((attr != INVALID_FILE_ATTRIBUTES)
        && ((attr & FILE_ATTRIBUTE_ARCHIVE) != 0)
        && ((attr & FILE_ATTRIBUTE_DIRECTORY) == 0));
    return ret;
}

std::string path_join(const std::vector<std::string>& items)
{
    std::stringstream ss;

    for (size_t i = 0; i < items.size(); i++)
    {
        std::string item = str_replace(items[i], '/', '\\');
        ss << item;
        if (((i + 1) < items.size()) && (!str_ends_with(item, "\\")))
        {
            ss << "\\";
        }
    }

    return ss.str();
}

std::vector<std::string> path_split(const std::string& pathname)
{
    std::vector<std::string> items;

    std::vector<std::string> items_t = str_split(str_replace(pathname, '/', '\\'), '\\');
    for (std::vector<std::string>::const_iterator it = items_t.begin(); it != items_t.end(); it++)
    {
        if (!it->empty())
        {
            items.push_back(*it);
        }
    }

    return items;
}

std::vector<std::string> path_splitext(const std::string& pathname)
{
    std::vector<std::string> items;
    size_t last_dot_index = pathname.find_last_of('.');
    if (last_dot_index >= 0)
    {
        items.push_back(pathname.substr(0, last_dot_index));
        items.push_back(pathname.substr(last_dot_index + 1));
    }
    else
    {
        items.push_back(pathname);
        items.push_back("");
    }
    return items;
}

//////////////////////////////////////////////////////////////////////////

std::vector<std::string> file_readlines(const std::string& filename)
{
    std::vector<std::string> lines;

    std::ifstream ifs(filename.c_str(), std::ios::in);
    if (ifs.is_open())
    {
        while (!ifs.eof())
        {
            char linebuf[1024] = { 0 };
            ifs.getline(linebuf, 1024);
            lines.push_back(linebuf);
        }
    }

    return lines;
}
