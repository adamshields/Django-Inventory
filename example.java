public DesignsModel addApprovalToDesign(Integer designId, Approval approval, String level) throws Exception {
    DesignsModel design = designsRepo.findById(designId)
            .orElseThrow(() -> new Exception("Design not found with id: " + designId));

    if (!approval.getApprovalLevel().equalsIgnoreCase(level)) {
        throw new Exception("Approval level in the request does not match the endpoint.");
    }

    boolean approvalUpdated = false;
    for (Approval existingApproval : design.getApprovals()) {
        if (existingApproval.getApprovalLevel().equalsIgnoreCase(approval.getApprovalLevel())) {
            if (existingApproval.getApprover() != null) {
                throw new Exception("Approval with level " + approval.getApprovalLevel() + " already exists.");
            }
            existingApproval.setApprover(SecurityContextHolder.getContext().getAuthentication().getName());
            existingApproval.setApprovedDate(LocalDateTime.now());
            approvalUpdated = true;
            break;
        }
    }

    if (!approvalUpdated) {
        throw new Exception("Approval with level " + approval.getApprovalLevel() + " does not exist.");
    }

    designsRepo.save(design);
    return design;
}
