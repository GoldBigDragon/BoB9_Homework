#pragma once

#include <vector>

static const int g_nMaxSwitchSize = 100;
struct ST_QUEST_FLAG_FILTER
{
	unsigned char mask[g_nMaxSwitchSize];
	unsigned char flags[g_nMaxSwitchSize];

	ST_QUEST_FLAG_FILTER(void)
		: mask{ 0, }
		, flags{ 0, }
	{}
	void Clear(void)
	{
		memset(mask, 0, g_nMaxSwitchSize);
		memset(flags, 0, g_nMaxSwitchSize);
	}
};

struct ST_USER_QUESTINFO
{
	unsigned char flags[g_nMaxSwitchSize];
	unsigned short values[g_nMaxSwitchSize];

	ST_USER_QUESTINFO(void)
		: flags{ 0, }, values{ 0, }
	{}

	bool Check(const ST_QUEST_FLAG_FILTER& other) const
	{
		int i;
		for (i = 0; i < g_nMaxSwitchSize; i++)
		{
			const unsigned char filter = other.flags[i] & other.mask[i];
			if ((flags[i] & filter) != filter)
				return false;
		}
		return true;
	}
	void Apply(const ST_QUEST_FLAG_FILTER& other)
	{
		int i;
		for (i = 0; i < g_nMaxSwitchSize; i++)
		{
			const unsigned char filter = other.flags[i] & other.mask[i];
			flags[i] |= filter;
		}
	}
};

struct ST_NPC_INFO
{
	int id;
	char szName[21];
	double x;
	double y;
	double w;
	double h;
	char patch;
	char szGreetMessage[61];

	ST_NPC_INFO(void)
		: id(0), szName{ 0, }, x(0), y(0), w(0), h(0), szGreetMessage{ 0, }
	{}
};

static const int g_nMaxMessageSize = 60;
struct ST_NPC_MESSAGE
{
	int nNpcID;	// 0 : User
	char szMessage[g_nMaxMessageSize + 1];

	ST_NPC_MESSAGE(void) {}
	ST_NPC_MESSAGE(int id, const char* pszMessage)
		: nNpcID(id), szMessage{ 0, }
	{
		strcpy_s(szMessage, g_nMaxMessageSize, pszMessage);
	}
};

enum E_QUEST_SEQUENCE_TYPE
{
	QUEST_SEQUENCE_TYPE_MESSAGE = 0,
	QUEST_SEQUENCE_TYPE_CONDITION,
	QUEST_SEQUENCE_TYPE_REWARD
};
struct ST_QUEST_SEQUENCE
{
	unsigned char nType;	// 0 : Message, 1 : filter
	union
	{
		ST_NPC_MESSAGE message;
		ST_QUEST_FLAG_FILTER filter;
	};

	ST_QUEST_SEQUENCE(void) {}
	ST_QUEST_SEQUENCE(int id, const char* pszMessage)
		: nType(QUEST_SEQUENCE_TYPE_MESSAGE)
	{
		message.nNpcID = id;
		strcpy_s(message.szMessage, g_nMaxMessageSize, pszMessage);
	}
	ST_QUEST_SEQUENCE(E_QUEST_SEQUENCE_TYPE type, const ST_QUEST_FLAG_FILTER& inFilter)
		: nType(type)
	{
		filter = inFilter;
	}
};

