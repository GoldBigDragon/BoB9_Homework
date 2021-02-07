#include "stdafx.h"
#include "QuestInfoSuper.h"

CQuestInfoSuper::CQuestInfoSuper(void)
	: m_nTargetNpcId(0)
	, m_nIndex(0)
{
}

CQuestInfoSuper::~CQuestInfoSuper(void)
{
}

int CQuestInfoSuper::GetID(void)
{
	return m_nTargetNpcId;
}

void CQuestInfoSuper::Check(ST_USER_QUESTINFO& userInfo, std::vector<ST_NPC_MESSAGE>& outMessage)
{
	while (m_nIndex < (int)m_Sequence.size())
	{
		ST_QUEST_SEQUENCE& seq = m_Sequence[m_nIndex];
		if (QUEST_SEQUENCE_TYPE_MESSAGE == seq.nType)
			outMessage.push_back(seq.message);

		if (QUEST_SEQUENCE_TYPE_REWARD == seq.nType)
			userInfo.Apply(seq.filter);

		if (QUEST_SEQUENCE_TYPE_CONDITION == seq.nType && !userInfo.Check(seq.filter))
			break;

		m_nIndex++;
	}

	// 조건에 걸려서 아무런 대화를 담을 수 없다면 직전 대화를 찾아서 넣어줌
	if (!outMessage.empty())
		return;

	int i;
	for (i = m_nIndex-1; 0 <= i; i--)
	{
		if (QUEST_SEQUENCE_TYPE_MESSAGE != m_Sequence[i].nType)
			continue;

		outMessage.push_back(m_Sequence[i].message);
		break;
	}

	// 실수로 메시지를 만들지 않은 퀘스트에는 주의를 줌
	if (outMessage.empty())
		outMessage.push_back(ST_NPC_MESSAGE(0, "** 아무 메시지가 없습니다. 버그 같아요..~ **"));
}
