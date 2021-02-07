#pragma once

#include "../QuestFramework/QuestFramework.h"

class PressPlateX : public CQuestInfoSuper
{
public:
	PressPlateX(void);
	~PressPlateX(void);

	bool IsCleared(const ST_USER_QUESTINFO& info);
};

