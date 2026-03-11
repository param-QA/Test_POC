const UserProfile = ({ userBio }: { userBio: string }) => {
  return (
    // Trigger: dangerouslySetInnerHTML bypasses XSS protection
    <div dangerouslySetInnerHTML={{ __html: userBio }} />
  );
};
