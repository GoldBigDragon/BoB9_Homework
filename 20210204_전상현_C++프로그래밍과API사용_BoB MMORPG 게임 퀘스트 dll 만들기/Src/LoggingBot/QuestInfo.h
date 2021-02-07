#pragma once

#include "../QuestFramework/IQuestInfo.h"

class CQuestInfo : public IQuestInfo
{
public:
	CQuestInfo(void);
	~CQuestInfo(void);

	void QueryNpc(std::vector<ST_NPC_INFO>& vecNPC);
	void QueryQuest(std::vector<CQuestInfoSuper*>& vecQuest);
};

