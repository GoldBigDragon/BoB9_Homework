#pragma once

#include <vector>
#include "Struct.h"
#include "QuestInfoSuper.h"
#include "IQuestInfo.h"

#define DLL_API extern "C" __declspec(dllexport)

void ExportDllMain(void);
void ExportAPIEntry(IQuestInfo* pIntance);

DLL_API int QueryNpc(ST_NPC_INFO* outInfoArr);
DLL_API int QueryQuest(CQuestInfoSuper** outInfoArr);
