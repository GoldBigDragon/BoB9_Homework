#pragma once

#include "../QuestFramework/QuestFramework.h"

class CProfrogQuest : public CQuestInfoSuper
{
	ST_QUEST_FLAG_FILTER m_ClearCondition;
public:
	CProfrogQuest(void);
	~CProfrogQuest(void);

	bool IsCleared(const ST_USER_QUESTINFO& info);
};
