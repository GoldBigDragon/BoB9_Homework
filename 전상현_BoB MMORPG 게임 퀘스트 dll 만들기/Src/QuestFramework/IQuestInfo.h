#pragma once

#include <vector>
#include "Struct.h"
#include "QuestInfoSuper.h"

struct IQuestInfo
{
	virtual void QueryNpc(std::vector<ST_NPC_INFO>& vecNPC) = 0;
	virtual void QueryQuest(std::vector<CQuestInfoSuper*>& vecQuest) = 0;
};
