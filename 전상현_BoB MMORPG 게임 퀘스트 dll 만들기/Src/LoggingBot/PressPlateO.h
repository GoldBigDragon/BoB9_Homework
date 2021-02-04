#pragma once

#include "../QuestFramework/QuestFramework.h"

class PressPlateO : public CQuestInfoSuper
{
public:
	PressPlateO(void);
	~PressPlateO(void);

	bool IsCleared(const ST_USER_QUESTINFO& info);
};

