#include "stdafx.h"
#include "PressPlateO.h"

PressPlateO::PressPlateO(void)
	: CQuestInfoSuper()
{
	m_nTargetNpcId = 10012;

	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(O이 적힌 낡은 감압판. 신호 1을 전송하는 것 같다.)"));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00000001;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00000011;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(O 글자가 적힌 감압판 위에 섰다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "고맙다 휴-먼."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "휴-먼의 레지스트리 파라미터 수정을 시작하겠다."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "준비가 되었다면 나에게 신호를 줘라. 휴-먼."));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00000111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00001111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(실력 향상을 위해서라도 해야 한다고 생각했다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[상태 : 양호.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[비고 : 1차 교육 과제도 TOP 30에 영향을 준다.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "내 옆의 파란 플로피디스크를 넣어라. 휴-먼."));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00011111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(당연히 더 우선한다고 생각했다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[상태 : 교정 필요.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[비고 : 교육부 정책이 우선한다.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[상태 : 교정 완료.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "내 옆의 녹색 CD를 넣어라. 휴-먼."));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b01111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(당연히 볼 수 있을거라 생각했다.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[상태 : 양호.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[비고 : https://quickconnect.to/bobtop]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[비고 : ID: 공통    PW : (ws^JQ   ]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "휴먼의 모든 레지스트리 교정이 끝났다. 수고했다."));
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b11111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
}

PressPlateO::~PressPlateO(void)
{
}

bool PressPlateO::IsCleared(const ST_USER_QUESTINFO& info)
{
	int nExitCode = system("calc.exe");
	if (0 == nExitCode)
		return true;
	return false;
}
