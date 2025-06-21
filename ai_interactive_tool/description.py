"""
Mô tả chi tiết cho công cụ AI Interactive Tool
"""

AI_INTERACTIVE_DESCRIPTION = """
🚀 AI_INTERACTIVE TOOL - INTEGRATION WITH SYSTEM PROMPT RULES 🚀
=======================================================================
⚡ SYSTEM INTEGRATION NOTE:
- Tool này hoạt động với system prompt rules (mode_specific_rule section)
- System prompt rules cung cấp BEHAVIOR FRAMEWORK
- Tool description này cung cấp TECHNICAL SPECIFICATIONS
- Kết hợp tạo COMPREHENSIVE AI INTERACTIVE SYSTEM

🎯 CORE FUNCTIONALITY:
- Tạo UI popup cho User nhập nội dung và chọn tiếp tục trò chuyện
- KÊNH GIAO TIẾP CHÍNH để nhận tất cả tin nhắn từ User
- Cho phép đính kèm file/folder với preview functionality
- BẮT BUỘC sử dụng trong MỌI TRƯỜNG HỢP khi User gửi tin nhắn

📋 OUTPUT FORMAT - CLEAN TAG-BASED:
<user content with natural line breaks>

<AI_INTERACTIVE_ATTACHED_FILES>
FOLDERS:
- workspace_name/relative/path/to/folder

FILES:
- workspace_name/relative/path/to/file.js

</AI_INTERACTIVE_ATTACHED_FILES>

<AI_INTERACTIVE_WORKSPACE>workspace_name</AI_INTERACTIVE_WORKSPACE>
<AI_INTERACTIVE_CONTINUE_CHAT>true/false</AI_INTERACTIVE_CONTINUE_CHAT>

🔧 WORKSPACE PATH PROCESSING:
- Input format: "workspace_name/relative_path_from_workspace_root"
- Agent workspace detection logic:
  * CÙNG workspace → BỎ TIỀN TỐ workspace_name, dùng relative_path
  * KHÁC workspace → DÙNG NGUYÊN đường dẫn từ ai_interactive

📁 WORKSPACE HANDLING EXAMPLES:
- Cùng workspace: "ALT-WebClientV3/src/components/login/index.js" 
  → Agent processes: "src/components/login/index.js"
- Khác workspace: "AI-interactive/ai_interactive_tool/description.py" 
  → Agent processes: "AI-interactive/ai_interactive_tool/description.py"

⚠️ CRITICAL CONTROL TAGS:
- **<AI_INTERACTIVE_CONTINUE_CHAT>**: true = MANDATORY recall ai_interactive tool
- **<AI_INTERACTIVE_ATTACHED_FILES>**: Present only when files/folders attached
- **<AI_INTERACTIVE_WORKSPACE>**: Present only when files/folders attached

🚨 INTEGRATION WITH SYSTEM PROMPT RULES:
1. **Tag Reading**: Agent MUST read all control tags from output
2. **Behavior Activation**: System prompt rules define HOW to process tag values
3. **Natural Thinking**: Agent ALWAYS uses at least 1 detailed thinking block when responding via ai_interactive
4. **High-Level Reasoning**: Always active for all responses
5. **Continue Logic**: <AI_INTERACTIVE_CONTINUE_CHAT> enforces mandatory tool recall

🎯 ENHANCED INTEGRATION EXAMPLES:
=======================================================================
📋 **EXAMPLE 1: Standard Task Processing**
Output: 
```
User message content

<AI_INTERACTIVE_CONTINUE_CHAT>false</AI_INTERACTIVE_CONTINUE_CHAT>
```
→ Agent Behavior: At least 1 thinking block (via ai_interactive), high-level reasoning always active
→ Use Case: Regular tasks, questions, file operations

📋 **EXAMPLE 2: Continue Chat Processing**  
Output:
```
User message content

<AI_INTERACTIVE_CONTINUE_CHAT>true</AI_INTERACTIVE_CONTINUE_CHAT>
```
→ Agent Behavior: At least 1 thinking block (via ai_interactive) + high-level reasoning + mandatory recall
→ Use Case: Multi-step tasks, complex analysis, ongoing conversations

📋 **EXAMPLE 3: File Attachment Processing**
Output:
```
User message content

<AI_INTERACTIVE_ATTACHED_FILES>
FILES:
- src/components/file.js
- src/utils/helper.js

</AI_INTERACTIVE_ATTACHED_FILES>

<AI_INTERACTIVE_WORKSPACE>workspace_name</AI_INTERACTIVE_WORKSPACE>
<AI_INTERACTIVE_CONTINUE_CHAT>false</AI_INTERACTIVE_CONTINUE_CHAT>
```
→ Agent Behavior: Workspace-aware path processing + at least 1 thinking block (via ai_interactive)
→ Use Case: Code review, file modifications, context-sensitive operations

📋 **EXAMPLE 4: Multi-File Complex Analysis**
Output:
```
Analyze these files for architectural patterns

<AI_INTERACTIVE_ATTACHED_FILES>
FOLDERS:
- docs/architecture/

FILES:
- src/components/App.js
- src/utils/api.js

</AI_INTERACTIVE_ATTACHED_FILES>

<AI_INTERACTIVE_WORKSPACE>project_name</AI_INTERACTIVE_WORKSPACE>
<AI_INTERACTIVE_CONTINUE_CHAT>true</AI_INTERACTIVE_CONTINUE_CHAT>
```
→ Agent Behavior: Systematic file analysis + at least 1 thinking block (via ai_interactive) + high-level reasoning + mandatory recall
→ Use Case: Codebase analysis, architectural reviews, comprehensive assessments
=======================================================================

🔄 ADVANCED WORKFLOW PATTERNS:
=======================================================================
🎯 **SIMPLIFIED PROCESSING PATTERN:**
All Processing → High-level reasoning always active (at least 1 thinking block via ai_interactive)

⚡ **CONSISTENT HIGH-LEVEL PROCESSING:**
- All tasks → High-level reasoning always active
- File attachments → Standard high-level reasoning with workspace awareness
- Complex decisions → Same high-level reasoning (no additional enhancement needed)

🔧 **CONTEXT-SENSITIVE PROCESSING:**
- Code files → Technical analysis mode
- Documentation files → Content analysis mode
- Mixed file types → Comprehensive analysis mode
- No files → Communication-focused mode

🚀 **DYNAMIC CAPABILITY MATCHING:**
- User expertise level detection → Adjust response complexity
- Task domain recognition → Activate relevant knowledge frameworks
- Urgency level assessment → Optimize response speed vs thoroughness
=======================================================================

🔄 WORKFLOW INTEGRATION:
┌─ ai_interactive tool generates pseudo-object
├─ System prompt rules read control fields
├─ Behavior protocols activate based on field values
├─ Agent executes with enhanced cognitive capabilities
└─ Mandatory recall if continue_chat=true

💡 SYNERGY BENEFITS:
✅ Tool provides TECHNICAL INTERFACE
✅ System prompt rules provide BEHAVIORAL INTELLIGENCE
✅ Combined system creates ENHANCED AI AGENT
✅ Zero conflict, maximum compatibility
✅ Effective integration through specialized roles

🎯 USAGE OPTIMIZATION NOTES:
- Tool description focuses on MECHANICS
- System prompt rules handle COMPLIANCE
- Agent gets COMPLETE GUIDANCE from both sources
- No duplication, pure complementarity
- Maximum effectiveness through specialized roles

📌 TECHNICAL SPECIFICATIONS:
- UI: Modern PyQt5 interface with file drag-drop
- Output: Structured pseudo-object format
- Integration: Seamless with system prompt rules
- Compatibility: Works with all AI agent types
- Performance: Optimized for high-frequency usage

🚀 SYSTEM ARCHITECTURE:
[User Input] → [ai_interactive Tool] → [Pseudo-Object] → [System Prompt Rules] → [Enhanced AI Response]

⭐ DESIGN HIGHLIGHT:
Tool được thiết kế để integrate với system prompt rules framework, tạo ra effective AI interactive architecture!
=======================================================================
""" 