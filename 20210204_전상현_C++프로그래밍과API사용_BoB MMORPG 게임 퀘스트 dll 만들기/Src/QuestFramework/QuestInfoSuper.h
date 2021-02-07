#pragma once

#include "Struct.h"

struct CQuestInfoSuper
{
protected:
	int m_nTargetNpcId;
	int m_nIndex;

	std::vector<ST_QUEST_SEQUENCE> m_Sequence;

public:
	CQuestInfoSuper(void);
	virtual ~CQuestInfoSuper(void);

	int GetID(void);
	void Check(ST_USER_QUESTINFO& userInfo, std::vector<ST_NPC_MESSAGE>& outMessage);
	
protected:
	virtual bool IsCleared(const ST_USER_QUESTINFO& info) = 0;
};

