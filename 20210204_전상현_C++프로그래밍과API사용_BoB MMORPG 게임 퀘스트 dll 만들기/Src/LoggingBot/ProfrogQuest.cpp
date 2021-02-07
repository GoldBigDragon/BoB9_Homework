#include "stdafx.h"
#include "ProfrogQuest.h"

CProfrogQuest::CProfrogQuest(void)
	: CQuestInfoSuper()
{
	m_nTargetNpcId = 7;

	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�ָ��� ���� �� ���� �������� �˾Ҵµ�)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�����̼� ���� ���� ���� �޸� ��ö �κ��̴�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(���̾� �� �κ��� �ü��� ���� ���ߴ�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "BoB ��Ȱ�� ����ֳ�, ��-��?"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(���� ������ ������ ���ٰ� ���ϰ� �;�����)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(��ó�� ���� ���� ���� �ֽ� �¿���ô �׷��ٰ� �Ͽ���.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "���� ������ ������̶� ������ Ȯ���� 99.87%���µ�"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "���� ���� ��ö�� �� �� ����̴�. ��-��"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(..?)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "�߿��� ������Ʈ�� �ߴܵǱ� ���� �޸� �� �����͸�"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "���������� ���� �ؾ� �� �ʿ䰡 �ְڴ�. ��-��."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "Ȥ�� �� �κ��� �����͸� �޾� �� ������ �ֳ�? ��-��."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "�Ƴ��α����� ��ȭ ����� ó�� �� �� ������,"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "�տ� ���̴� O, X ���� ������ ���� ���� ��ȣ�� �ض�. ��-��."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(O, X ������ ���� ���� �� �ǰ��� ������ ����..!)"));
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
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "[Q. 1�� ���� �Ⱓ�� �� �ִ� ������ ���� �ʾƵ� �ȴ�. (O/X)]"));
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
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�溿�� �����⿡ �÷��ǵ�ũ�� ������.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(���� �ϴ��� �ȵ��̰� �������� ���� �б� �����̴�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...���� �� �����ΰž�...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "[Q. BoB ������ ����б� �������� �켱�ȴ�. (O/X)]"));
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
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�溿�� �����⿡ CD�� �־���.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�󺧿� CD-R�̶� ������ ���� �б� �����̴�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...������ ���� CD-R�� �־� �ٴѴٴ���...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "[Q. BoB NAS���� 9�� ���� �ڷḦ ���� �� �ִ�. (O/X)]"));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b11111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "���ڻ���. ����� ���. �ʱ��ϴ� ������ ������ ��-��."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...�װ� �� ���� �ƴѵ�...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(...�׷��� ���� ���ǲ�� �´� �� �� ������ ���...)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(m_nTargetNpcId, "���ڻ���. ����� ���. �ʱ��ϴ� ������ ������ ��-��."));
}

CProfrogQuest::~CProfrogQuest(void)
{
}

bool CProfrogQuest::IsCleared(const ST_USER_QUESTINFO& info)
{
	return info.Check(m_ClearCondition);
}
