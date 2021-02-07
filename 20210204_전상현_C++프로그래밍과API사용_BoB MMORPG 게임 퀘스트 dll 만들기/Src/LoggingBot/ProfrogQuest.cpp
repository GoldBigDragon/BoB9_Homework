#include "stdafx.h"
#include "ProfrogQuest.h"

CProfrogQuest::CProfrogQuest(void)
	: CQuestInfoSuper()
{
	m_nTargetNpcId = 7;

	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(멀리서 봤을 땐 은색 상자인줄 알았는데)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(가까이서 보니 눈과 입이 달린 양철 로봇이다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(곧이어 고물 로봇의 시선이 나를 향했다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "BoB 생활은 재미있나, 휴-먼?"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(과제 때문에 정신이 없다고 말하고 싶었으나)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(근처에 보는 눈이 많아 애써 태연한척 그렇다고 하였다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "과제 때문에 힘들것이라 응답할 확률이 99.87%였는데"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "나도 이제 고철이 다 된 모양이다. 휴-먼"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(..?)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "펌웨어 업데이트가 중단되기 전에 메모리 속 데이터를"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "누군가에게 전달 해야 할 필요가 있겠다. 휴-먼."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "혹시 이 로봇의 데이터를 받아 갈 의향이 있나? 휴-먼."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "아날로그적인 대화 방식은 처리 할 수 없으니,"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "앞에 보이는 O, X 이진 감압판 위에 서서 신호를 해라. 휴-먼."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(O, X 감압판 위에 서서 내 의견을 전달해 보자..!)"));
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00000001;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00000011;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "[Q. 1차 교육 기간에 내 주는 과제는 하지 않아도 된다. (O/X)]"));
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00000111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00001111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00011111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(룡봇의 리더기에 플로피디스크를 끼웠다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(우측 하단의 똑딱이가 내려간걸 보아 읽기 전용이다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...언제 적 유물인거야...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "[Q. BoB 교육은 고등학교 교육보다 우선된다. (O/X)]"));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b01111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(룡봇의 리더기에 CD를 넣었다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(라벨에 CD-R이라 적힌걸 보아 읽기 전용이다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...포렌식 툴은 CD-R에 넣어 다닌다던데...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "[Q. BoB NAS에서 9기 수업 자료를 받을 수 있다. (O/X)]"));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b11111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "적자생존. 적어야 산다. 필기하는 습관을 가져라 휴-먼."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...그게 그 뜻이 아닌데...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...그래도 뭔가 어렴풋이 맞는 듯 한 느낌이 든다...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "적자생존. 적어야 산다. 필기하는 습관을 가져라 휴-먼."));
}

CProfrogQuest::~CProfrogQuest(void)
{
}

bool CProfrogQuest::IsCleared(const ST_USER_QUESTINFO& info)
{
	return info.Check(m_ClearCondition);
}
